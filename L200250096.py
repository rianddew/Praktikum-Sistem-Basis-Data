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
# TAMBAH DISTRIBUTOR
# =====================================

def tambah_distributor():

    #clear()

    print("=" * 50)
    print(" TAMBAH DATA DISTRIBUTOR ")
    print("=" * 50)

    nama = input("Nama Distributor : ")
    alamat = input("Alamat           : ")
    kontak = input("Kontak           : ")
    email = input("Email            : ")
    wilayah = input("Wilayah Distribusi : ")

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO distributor
    (
        nama,
        alamat,
        kontak,
        email,
        wilayah_distribusi
    )
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(
        sql,
        (
            nama,
            alamat,
            kontak,
            email,
            wilayah
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("\n[SUKSES] Distributor berhasil ditambahkan.")

    pause()


# =====================================
# TAMPIL DISTRIBUTOR
# =====================================

def tampil_distributor():

    #clear()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM distributor
    """)

    data = cursor.fetchall()

    print("=" * 130)
    print("DATA DISTRIBUTOR")
    print("=" * 130)

    print(
        f"{'ID':<5}"
        f"{'Nama':<35}"
        f"{'Alamat':<20}"
        f"{'Kontak':<18}"
        f"{'Email':<35}"
        f"{'Wilayah':<20}"
    )

    print("-" * 130)

    for row in data:

        print(
            f"{row[0]:<5}"
            f"{row[1]:<35}"
            f"{row[2]:<20}"
            f"{row[3]:<18}"
            f"{row[4]:<35}"
            f"{row[5]:<20}"
        )

    cursor.close()
    conn.close()

    pause()


# =====================================
# UPDATE DISTRIBUTOR
# =====================================

def update_distributor():

    #clear()

    print("=" * 50)
    print(" UPDATE DATA DISTRIBUTOR ")
    print("=" * 50)

    id_distributor = input("ID Distributor : ")

    nama = input("Nama Baru       : ")
    alamat = input("Alamat Baru     : ")
    kontak = input("Kontak Baru     : ")
    email = input("Email Baru      : ")
    wilayah = input("Wilayah Baru    : ")

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE distributor
    SET
        nama=%s,
        alamat=%s,
        kontak=%s,
        email=%s,
        wilayah_distribusi=%s
    WHERE id_distributor=%s
    """

    cursor.execute(
        sql,
        (
            nama,
            alamat,
            kontak,
            email,
            wilayah,
            id_distributor
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("\n[SUKSES] Distributor berhasil diupdate.")

    pause()


# =====================================
# HAPUS DISTRIBUTOR
# =====================================

def hapus_distributor():

    #clear()

    print("=" * 50)
    print(" HAPUS DATA DISTRIBUTOR ")
    print("=" * 50)

    id_distributor = input("ID Distributor : ")

    konfirmasi = input(
        "Yakin ingin menghapus data? (y/n): "
    )

    if konfirmasi.lower() != "y":
        return

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    DELETE FROM distributor
    WHERE id_distributor=%s
    """

    cursor.execute(sql, (id_distributor,))

    conn.commit()

    cursor.close()
    conn.close()

    print("\n[SUKSES] Distributor berhasil dihapus.")

    pause()


# =====================================
# MENU DISTRIBUTOR
# =====================================

def menu_distributor():

    while True:

        #clear()

        print("=" * 50)
        print(" MENU DISTRIBUTOR ")
        print("=" * 50)

        print("1. Registrasi Distributor")
        print("2. Data Distributor")
        print("3. Perbarui Data Distributor")
        print("4. Hapus Data Distributor")
        print("0. Kembali")

        pilih = input("\nPilih Menu : ")

        if pilih == "1":
            tambah_distributor()

        elif pilih == "2":
            tampil_distributor()

        elif pilih == "3":
            update_distributor()

        elif pilih == "4":
            hapus_distributor()

        elif pilih == "0":
            break

        else:
            print("\nMenu tidak tersedia.")
            pause()