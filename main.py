from L200250033 import menu_produk
from L200250096 import menu_distributor
from L200250098 import menu_lini
from L200250026 import menu_pesanan
from L200254102 import menu_laporan
from db import reset_database

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
# DASHBOARD UTAMA
# =====================================

def main():

    while True:

        #clear()

        print("=" * 70)
        print("      SISTEM MANAJEMEN PRODUKSI PABRIK")
        print("=" * 70)

        print("1. Kelola Produk")
        print("2. Kelola Distributor")
        print("3. Kelola Lini Produksi")
        print("4. Transaksi Pesanan")
        print("5. Laporan")
        print("6. Reset Database")
        print("0. Keluar")

        print("-" * 70)

        pilihan = input("Pilih Menu : ")

        # ==========================
        # PRODUK
        # ==========================

        if pilihan == "1":
            menu_produk()

        # ==========================
        # DISTRIBUTOR
        # ==========================

        elif pilihan == "2":
            menu_distributor()

        # ==========================
        # LINI PRODUKSI
        # ==========================

        elif pilihan == "3":
            menu_lini()

        # ==========================
        # PESANAN
        # ==========================

        elif pilihan == "4":
            menu_pesanan()

        # ==========================
        # LAPORAN
        # ==========================

        elif pilihan == "5":
            menu_laporan()

        # ==========================
        # RESET DATABASE
        # ==========================

        elif pilihan == "6":

            clear()

            print("=" * 60)
            print(" RESET DATABASE ")
            print("=" * 60)

            print(
                "\nPERINGATAN!\n"
                "Semua data akan dihapus "
                "dan ID akan kembali ke 1."
            )

            konfirmasi = input(
                "\nLanjutkan? (y/n) : "
            )

            if konfirmasi.lower() == "y":

                reset_database()

                print(
                    "\nDatabase berhasil direset."
                )

            else:

                print(
                    "\nReset dibatalkan."
                )

            pause()

        # ==========================
        # KELUAR
        # ==========================

        elif pilihan == "0":

            #clear()

            print("=" * 60)
            print(" TERIMA KASIH ")
            print("=" * 60)

            print(
                "\nProgram selesai."
            )

            break

        # ==========================
        # MENU TIDAK VALID
        # ==========================

        else:

            print("\nMenu tidak tersedia.")
            pause()


# =====================================
# PROGRAM UTAMA
# =====================================

if __name__ == "__main__":
    main()