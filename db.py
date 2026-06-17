import mysql.connector


def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="factory",
            port=3306
        )
        return conn

    except mysql.connector.Error as err:
        print("\n===================================")
        print("GAGAL TERHUBUNG KE DATABASE")
        print("===================================")
        print("Error :", err)
        print("\nPastikan:")
        print("1. XAMPP MySQL sudah dijalankan")
        print("2. Database 'factory' sudah dibuat")
        print("3. File kelompok.sql sudah di-import")
        print("===================================")

        return None


def execute_query(query, data=None):
    """
    Untuk INSERT, UPDATE, DELETE
    """

    conn = get_connection()

    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)

        conn.commit()

        return True

    except mysql.connector.Error as err:

        print("\nError :", err)
        return False

    finally:

        cursor.close()
        conn.close()


def fetch_all(query, data=None):
    """
    Untuk SELECT banyak data
    """

    conn = get_connection()

    if conn is None:
        return []

    try:

        cursor = conn.cursor()

        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)

        hasil = cursor.fetchall()

        return hasil

    except mysql.connector.Error as err:

        print("\nError :", err)
        return []

    finally:

        cursor.close()
        conn.close()


def fetch_one(query, data=None):
    """
    Untuk SELECT satu data
    """

    conn = get_connection()

    if conn is None:
        return None

    try:

        cursor = conn.cursor()

        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)

        hasil = cursor.fetchone()

        return hasil

    except mysql.connector.Error as err:

        print("\nError :", err)
        return None

    finally:

        cursor.close()
        conn.close()


def reset_database():
    """
    Menghapus seluruh data dan reset AUTO_INCREMENT
    """

    conn = get_connection()

    if conn is None:
        return False

    try:

        cursor = conn.cursor()

        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

        cursor.execute("TRUNCATE TABLE detail_pesanan")
        cursor.execute("TRUNCATE TABLE jadwal_produksi")
        cursor.execute("TRUNCATE TABLE pesanan")
        cursor.execute("TRUNCATE TABLE produk")
        cursor.execute("TRUNCATE TABLE distributor")
        cursor.execute("TRUNCATE TABLE lini_produksi")

        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        conn.commit()

        print("\nDatabase berhasil direset.")

        return True

    except mysql.connector.Error as err:

        print("\nError :", err)
        return False

    finally:

        cursor.close()
        conn.close()