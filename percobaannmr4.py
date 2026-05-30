from datetime import date, datetime, timedelta
import mysql.connector
 
cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
tanggal = datetime.now().date()
tambah_transaksi = ("INSERT INTO transaksi (id_nasabahFK, no_rekeningFK, jenis_transaksi, tanggal, jumlah) VALUES (%s, %s, %s, %s, %s)")
data_transaksi = ('9', '110','kredit', tanggal, '50000')
cursor.execute(tambah_transaksi, data_transaksi)

cnx.commit()
cursor.close()
cnx.close()