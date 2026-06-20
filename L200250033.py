from db import get_connection
import os


# =====================================
# FUNGSI BANTU
# =====================================

def clear():
    #os.system("cls" if os.name == "nt" else "clear")
    pass

def pause():
    input("\nTekan ENTER untuk melanjutkan...")


# =====================================
# TAMBAH PRODUK
# =====================================

def tambah_produk():

    #clear()

    print("=" * 50)
    print(" TAMBAH DATA PRODUK ")
    print("=" * 50)

    nama = input("Nama Produk            : ")
    jenis = input("Jenis Produk           : ")
    stok = int(input("Jumlah Stok            : "))
    biaya = float(input("Biaya Produksi / Unit  : "))

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO produk
    (
        nama_produk,
        jenis,
        jumlah_stok,
        biaya_produksi_per_unit
    )
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(
        sql,
        (nama, jenis, stok, biaya)
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("\n[SUKSES] Produk berhasil ditambahkan.")

    pause()


# =====================================
# TAMPIL PRODUK
# =====================================

def tampil_produk():

    #clear()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM produk
    """)

    data = cursor.fetchall()

    print("=" * 95)
    print("DATA PRODUK")
    print("=" * 95)

    print(
        f"{'ID':<5}"
        f"{'Nama Produk':<30}"
        f"{'Jenis':<20}"
        f"{'Stok':<10}"
        f"{'Biaya Produksi':<20}"
    )

    print("-" * 95)

    for row in data:

        print(
            f"{row[0]:<5}"
            f"{row[1]:<30}"
            f"{row[2]:<20}"
            f"{row[3]:<10}"
            f"Rp {float(row[4]):,.2f}"
        )

    cursor.close()
    conn.close()

    pause()


# =====================================
# UPDATE PRODUK
# =====================================

def update_produk():

    #clear()

    print("=" * 50)
    print(" UPDATE DATA PRODUK ")
    print("=" * 50)

    id_produk = input("ID Produk yang diubah : ")

    nama = input("Nama Baru             : ")
    jenis = input("Jenis Baru            : ")
    stok = int(input("Stok Baru             : "))
    biaya = float(input("Biaya Baru            : "))

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE produk
    SET
        nama_produk=%s,
        jenis=%s,
        jumlah_stok=%s,
        biaya_produksi_per_unit=%s
    WHERE id_produk=%s
    """

    cursor.execute(
        sql,
        (
            nama,
            jenis,
            stok,
            biaya,
            id_produk
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("\n[SUKSES] Produk berhasil diperbarui.")

    pause()


# =====================================
# HAPUS PRODUK
# =====================================

def hapus_produk():

    #clear()

    print("=" * 50)
    print(" HAPUS DATA PRODUK ")
    print("=" * 50)

    id_produk = input("ID Produk : ")

    konfirmasi = input(
        "Yakin ingin menghapus data? (y/n):"
    )

    if konfirmasi.lower() != "y":
        return

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    DELETE FROM produk
    WHERE id_produk=%s
    """

    cursor.execute(sql, (id_produk,))

    conn.commit()

    cursor.close()
    conn.close()

    print("\n[SUKSES] Produk berhasil dihapus.")

    pause()


# =====================================
# MENU PRODUK
# =====================================

def menu_produk():

    while True:

        #clear()

        print("=" * 50)
        print(" MENU PRODUK ")
        print("=" * 50)

        print("1. Registrasi Produk")
        print("2. Daftar Produk")
        print("3. Perbarui Data Produk")
        print("4. Hapus Data Produk")
        print("0. Kembali")

        pilih = input("\nPilih Menu : ")

        if pilih == "1":
            tambah_produk()

        elif pilih == "2":
            tampil_produk()

        elif pilih == "3":
            update_produk()

        elif pilih == "4":
            hapus_produk()

        elif pilih == "0":
            break

        else:
            print("\nMenu tidak tersedia.")
            pause()