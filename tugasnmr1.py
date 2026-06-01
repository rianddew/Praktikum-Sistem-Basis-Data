from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root',database='perbankan')
cursor = cnx.cursor()
tanggal = datetime.now().date()

# insert data ke tabel transaksi
tambah_transaksi = ("INSERT INTO transaksi (id_nasabahFK, no_rekeningFK, jenis_transaksi, tanggal, jumlah) VALUES (%s, %s, %s, %s, %s)")
data_transaksi = ('5', '107', 'debit', tanggal, '75000')
cursor.execute(tambah_transaksi, data_transaksi)
cnx.commit()

# update data ke tabel transaksi
update_transaksi = ("UPDATE transaksi SET jumlah = %s WHERE no_rekeningFK = %s AND jenis_transaksi = %s AND tanggal = %s")
data_update = ('50000', '103', 'debit', '2022-12-2')
cursor.execute(update_transaksi, data_update)
cnx.commit()

# delete data pada tabel transaksi
delete_transaksi = ("DELETE FROM transaksi WHERE no_rekeningFK = %s AND jenis_transaksi = %s AND tanggal = %s")
data_delete = ('110', 'debit', '2022-12-6')
cursor.execute(delete_transaksi, data_delete)
cnx.commit()

cursor.close()
cnx.close()
