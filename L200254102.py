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
# LAPORAN JOIN
# =====================================

def laporan_join():

    #clear()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        p.id_pesanan,
        d.nama,
        pr.nama_produk,
        dp.jumlah_pesan,
        dp.subtotal

    FROM pesanan p

    JOIN distributor d
        ON p.id_distributor = d.id_distributor

    JOIN detail_pesanan dp
        ON p.id_pesanan = dp.id_pesanan

    JOIN produk pr
        ON dp.id_produk = pr.id_produk

    ORDER BY p.id_pesanan
    """)

    data = cursor.fetchall()

    print("=" * 110)
    print("LAPORAN PESANAN")
    print("=" * 110)

    print(
        f"{'ID':<5}"
        f"{'Distributor':<35}"
        f"{'Produk':<25}"
        f"{'Jumlah':<15}"
        f"{'Subtotal':<20}"
    )

    print("-" * 110)

    for row in data:

        print(
            f"{row[0]:<5}"
            f"{row[1]:<35}"
            f"{row[2]:<25}"
            f"{row[3]:<15}"
            f"Rp {float(row[4]):,.2f}"
        )

    cursor.close()
    conn.close()

    pause()


# =====================================
# LAPORAN AGREGAT
# =====================================

def laporan_agregat():

    #clear()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        COUNT(*),
        SUM(total_harga),
        AVG(total_harga)
    FROM pesanan
    """)

    hasil = cursor.fetchone()

    print("=" * 60)
    print("Statistik Penjualan")
    print("=" * 60)

    print(
        f"Jumlah Pesanan       : {hasil[0]}"
    )

    print(
        f"Total Penjualan      : Rp {float(hasil[1] or 0):,.2f}"
    )

    print(
        f"Rata-rata Penjualan  : Rp {float(hasil[2] or 0):,.2f}"
    )

    cursor.close()
    conn.close()

    pause()


# =====================================
# LAPORAN JADWAL PRODUKSI
# =====================================

def laporan_jadwal():

    #clear()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        jp.id_jadwal,
        pr.nama_produk,
        lp.nama_lini,
        jp.tanggal_jadwal,
        jp.jumlah_target

    FROM jadwal_produksi jp

    JOIN produk pr
        ON jp.id_produk = pr.id_produk

    JOIN lini_produksi lp
        ON jp.id_lini = lp.id_lini

    ORDER BY jp.id_jadwal
    """)

    data = cursor.fetchall()

    print("=" * 120)
    print("JADWAL PRODUKSI")
    print("=" * 120)

    print(
        f"{'ID':<5}"
        f"{'Produk':<30}"
        f"{'Lini Produksi':<25}"
        f"{'Tanggal':<20}"
        f"{'Target':<15}"
    )

    print("-" * 120)

    for row in data:

        print(
            f"{row[0]:<5}"
            f"{row[1]:<30}"
            f"{row[2]:<25}"
            f"{str(row[3]):<20}"
            f"{row[4]:<15}"
        )

    cursor.close()
    conn.close()

    pause()


# =====================================
# MENU LAPORAN
# =====================================

def menu_laporan():

    while True:

        #clear()

        print("=" * 60)
        print(" MENU LAPORAN ")
        print("=" * 60)

        print("1. Laporan Pesanan")
        print("2. Statistik Penjualan")
        print("3. Jadwal Produksi")
        print("0. Kembali")

        pilih = input(
            "\nPilih Menu : "
        )

        if pilih == "1":
            laporan_join()

        elif pilih == "2":
            laporan_agregat()

        elif pilih == "3":
            laporan_jadwal()

        elif pilih == "0":
            break

        else:
            print("Menu tidak tersedia")
            pause()