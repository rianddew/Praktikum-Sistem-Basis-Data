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
# TAMBAH PESANAN
# =====================================

def tambah_pesanan():

    #clear()

    print("=" * 60)
    print(" TRANSAKSI PESANAN ")
    print("=" * 60)

    id_distributor = input("ID Distributor      : ")

    tanggal = input(
        "Tanggal Pesanan (YYYY-MM-DD) : "
    )

    pengiriman = input(
        "Tanggal Pengiriman (YYYY-MM-DD) : "
    )

    metode = input(
        "Metode Pembayaran : "
    )

    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # SIMPAN HEADER PESANAN
    # ==========================

    sql_pesanan = """
    INSERT INTO pesanan
    (
        id_distributor,
        tanggal_pesanan,
        jadwal_pengiriman,
        metode_pembayaran
    )
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(
        sql_pesanan,
        (
            id_distributor,
            tanggal,
            pengiriman,
            metode
        )
    )

    conn.commit()

    id_pesanan = cursor.lastrowid

    total_harga = 0

    # ==========================
    # INPUT DETAIL PESANAN
    # ==========================

    while True:

        print("\nMasukkan Produk")

        id_produk = input(
            "ID Produk (0 = selesai) : "
        )

        if id_produk == "0":
            break

        jumlah = int(
            input("Jumlah Pesan : ")
        )

        # Ambil harga produk

        cursor.execute("""
        SELECT biaya_produksi_per_unit
        FROM produk
        WHERE id_produk=%s
        """, (id_produk,))

        hasil = cursor.fetchone()

        if hasil is None:

            print("Produk tidak ditemukan.")
            continue

        harga = float(hasil[0])

        diskon = float(
            input("Diskon : ")
        )

        subtotal = (
            harga * jumlah
        ) - diskon

        total_harga += subtotal

        sql_detail = """
        INSERT INTO detail_pesanan
        (
            id_pesanan,
            id_produk,
            jumlah_pesan,
            harga_satuan,
            diskon,
            subtotal
        )
        VALUES
        (%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(
            sql_detail,
            (
                id_pesanan,
                id_produk,
                jumlah,
                harga,
                diskon,
                subtotal
            )
        )

        conn.commit()

        print(
            f"Subtotal = Rp {subtotal:,.2f}"
        )

    # ==========================
    # UPDATE TOTAL PESANAN
    # ==========================

    cursor.execute("""
    UPDATE pesanan
    SET total_harga=%s
    WHERE id_pesanan=%s
    """,
    (
        total_harga,
        id_pesanan
    ))

    conn.commit()

    print("\n================================")
    print("PESANAN BERHASIL DISIMPAN")
    print("================================")
    print("ID Pesanan :", id_pesanan)
    print(
        f"Total Harga : Rp {total_harga:,.2f}"
    )

    cursor.close()
    conn.close()

    pause()


# =====================================
# TAMPIL PESANAN
# =====================================

def tampil_pesanan():

    #clear()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        p.id_pesanan,
        d.nama,
        p.tanggal_pesanan,
        p.jadwal_pengiriman,
        p.status_pesanan,
        p.total_harga
    FROM pesanan p
    JOIN distributor d
        ON p.id_distributor=d.id_distributor
    ORDER BY p.id_pesanan
    """)

    data = cursor.fetchall()

    print("=" * 120)
    print("DATA PESANAN")
    print("=" * 120)

    print(
        f"{'ID':<5}"
        f"{'Distributor':<35}"
        f"{'Tanggal':<15}"
        f"{'Pengiriman':<15}"
        f"{'Status':<15}"
        f"{'Total Harga':<20}"
    )

    print("-" * 120)

    for row in data:

        print(
            f"{row[0]:<5}"
            f"{row[1]:<35}"
            f"{str(row[2]):<15}"
            f"{str(row[3]):<15}"
            f"{row[4]:<15}"
            f"Rp {float(row[5]):,.2f}"
        )

    cursor.close()
    conn.close()

    pause()


# =====================================
# HAPUS PESANAN
# =====================================

def hapus_pesanan():

    #clear()

    print("=" * 60)
    print(" HAPUS PESANAN ")
    print("=" * 60)

    id_pesanan = input(
        "ID Pesanan : "
    )

    konfirmasi = input(
        "Yakin hapus? (y/n) : "
    )

    if konfirmasi.lower() != "y":
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM pesanan
    WHERE id_pesanan=%s
    """, (id_pesanan,))

    conn.commit()

    cursor.close()
    conn.close()

    print("\nPesanan berhasil dihapus.")

    pause()


# =====================================
# MENU PESANAN
# =====================================

def menu_pesanan():

    while True:

        #clear()

        print("=" * 60)
        print(" MENU PESANAN ")
        print("=" * 60)

        print("1. Buat Pesanan")
        print("2. Daftar Pesanan")
        print("3. Batalkan Pesanan")
        print("0. Kembali")

        pilih = input(
            "\nPilih Menu : "
        )

        if pilih == "1":
            tambah_pesanan()

        elif pilih == "2":
            tampil_pesanan()

        elif pilih == "3":
            hapus_pesanan()

        elif pilih == "0":
            break

        else:
            print("Menu tidak tersedia")
            pause()