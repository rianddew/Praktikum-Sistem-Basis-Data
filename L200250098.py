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
# TAMBAH LINI PRODUKSI
# =====================================

def tambah_lini():

    #clear()

    print("=" * 60)
    print(" TAMBAH DATA LINI PRODUKSI ")
    print("=" * 60)

    nama = input("Nama Lini             : ")
    kapasitas = int(input("Kapasitas Produksi    : "))
    tenaga = int(input("Jumlah Tenaga Kerja   : "))
    status = input("Status (Aktif/Maintenance/Nonaktif) : ")
    lokasi = input("Lokasi Lini           : ")

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO lini_produksi
    (
        nama_lini,
        kapasitas_produksi,
        jumlah_tenaga_kerja,
        status_lini,
        lokasi_lini
    )
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(
        sql,
        (
            nama,
            kapasitas,
            tenaga,
            status,
            lokasi
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("\n[SUKSES] Lini produksi berhasil ditambahkan.")

    pause()


# =====================================
# TAMPIL LINI PRODUKSI
# =====================================

def tampil_lini():

    #clear()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM lini_produksi
    """)

    data = cursor.fetchall()

    print("=" * 110)
    print("DATA LINI PRODUKSI")
    print("=" * 110)

    print(
        f"{'ID':<5}"
        f"{'Nama Lini':<25}"
        f"{'Kapasitas':<15}"
        f"{'Tenaga Kerja':<15}"
        f"{'Status':<15}"
        f"{'Lokasi':<20}"
    )

    print("-" * 110)

    for row in data:

        print(
            f"{row[0]:<5}"
            f"{row[1]:<25}"
            f"{row[2]:<15}"
            f"{row[3]:<15}"
            f"{row[4]:<15}"
            f"{row[5]:<20}"
        )

    cursor.close()
    conn.close()

    pause()


# =====================================
# UPDATE LINI PRODUKSI
# =====================================

def update_lini():

    #clear()

    print("=" * 60)
    print(" UPDATE DATA LINI PRODUKSI ")
    print("=" * 60)

    id_lini = input("ID Lini              : ")

    nama = input("Nama Lini Baru       : ")
    kapasitas = int(input("Kapasitas Baru       : "))
    tenaga = int(input("Tenaga Kerja Baru    : "))
    status = input("Status Baru          : ")
    lokasi = input("Lokasi Baru          : ")

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE lini_produksi
    SET
        nama_lini=%s,
        kapasitas_produksi=%s,
        jumlah_tenaga_kerja=%s,
        status_lini=%s,
        lokasi_lini=%s
    WHERE id_lini=%s
    """

    cursor.execute(
        sql,
        (
            nama,
            kapasitas,
            tenaga,
            status,
            lokasi,
            id_lini
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("\n[SUKSES] Lini produksi berhasil diupdate.")

    pause()


# =====================================
# HAPUS LINI PRODUKSI
# =====================================

def hapus_lini():

    #clear()

    print("=" * 60)
    print(" HAPUS DATA LINI PRODUKSI ")
    print("=" * 60)

    id_lini = input("ID Lini : ")

    konfirmasi = input(
        "Yakin ingin menghapus data? (y/n): "
    )

    if konfirmasi.lower() != "y":
        return

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    DELETE FROM lini_produksi
    WHERE id_lini=%s
    """

    cursor.execute(sql, (id_lini,))

    conn.commit()

    cursor.close()
    conn.close()

    print("\n[SUKSES] Lini produksi berhasil dihapus.")

    pause()


# =====================================
# MENU LINI PRODUKSI
# =====================================

def menu_lini():

    while True:

        #clear()

        print("=" * 60)
        print(" MENU LINI PRODUKSI ")
        print("=" * 60)

        print("1. Registrasi Lini Produksi")
        print("2. Data Lini Produksi")
        print("3. Perbarui Data Lini Produksi")
        print("4. Hapus Data Lini Produksi")
        print("0. Kembali")

        pilih = input("\nPilih Menu : ")

        if pilih == "1":
            tambah_lini()

        elif pilih == "2":
            tampil_lini()

        elif pilih == "3":
            update_lini()

        elif pilih == "4":
            hapus_lini()

        elif pilih == "0":
            break

        else:
            print("\nMenu tidak tersedia.")
            pause()