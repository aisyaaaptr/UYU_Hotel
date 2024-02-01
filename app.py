import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456789",
    database="oyoo"
)


def input_data(db):
    nama_pemesan = input("Masukan nama pemesan: ")
    check_in = input("Masukan tanggal masuk/pemesanan: ")
    print("== Tipe kamar yang tersedia: ")
    print("1. Standar 1-15")
    print("2. VIP 16-25")
    print("3. VVIP 26-40")
    tipe_kamar = input("Tipe kamar yang dipilih: ")
    nomor_kamar = input("Nomor kamar: ")
    val=(nama_pemesan,check_in,tipe_kamar,nomor_kamar)
    mycursor = db.cursor()
    sql = "INSERT INTO data (nama_pemesan, check_in, tipe_kamar, nomor_kamar) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def show_data(db):
    mycursor = db.cursor()
    sql = "SELECT * FROM data"
    mycursor.execute(sql)
    results = mycursor.fetchall()

    if mycursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

def search_data(db):
    mycursor = db.cursor()
    keyword = input("Masukan tanggal check in: ")
    sql = "SELECT nama_pemesan, check_in, tipe_kamar, nomor_kamar FROM data WHERE check_in LIKE {}"
    val="\'%{}%\'".format(keyword)
    sql=sql.format(val)
    mycursor.execute(sql)
    results= mycursor.fetchall()

    if mycursor.rowcount < 0:
        print("tidak ada data")
    else:
        for data in results:
            print(data)
    
def show_menu(db):
    print("===+ APLIKASI PEMESANAN HOTEL UYU +===")
    print("1. Menu Registrasi")
    print("2. Menu Show")
    print("3. Menu Search")
    print("4. Home")
    print("------------------------")
    menu = input("Pilih menu> ")

    #clear screen
    
    if menu == "1":
        input_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        search_data(db)
    elif menu == "4":
        exit()
    else:
        print("Menu salah")

if __name__ == "__main__":
    while(True):
        show_menu(db)
