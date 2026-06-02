from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root',database='perbankan')
cursor = cnx.cursor()
query = ("SELECT id_nasabah, nama_nasabah, alamat_nasabah FROM nasabah")
cursor.execute(query)
for (id_nasabah, nama_nasabah, alamat_nasabah) in cursor:
    print("ID Nasabah : {} | Nama : {} | Alamat : {}"
        .format(id_nasabah, nama_nasabah, alamat_nasabah))

cursor.close()
cnx.close()
