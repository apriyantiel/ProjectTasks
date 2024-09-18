#LAYAR INPUT
def header()  :
  print(" ========== SOEKARNO HATTA AIRPORT ========== ")
  print("               TANGERANG, BANTEN              ")
  print("             TELP - (021) 63867867            ")

def listHargaTiket() :
  print("___________________________________________________")
  print("No | Kode Jurusan | Kota       | Harga Tiket     | ")
  print("___________________________________________________")
  print("1  | MDN/mdn      |  Medan     |   Rp. 2000000   |")
  print("2  | PDG/pdg      |  Padang    |   Rp. 2200000   |")
  print("3  | SMG/smg      | Semarang   |   Rp. 1200000   |")
  print("4  | YGY/ygy      | Yogyakarta |   Rp. 1500000   |")
  print("5  | JMB/jmb      | Jambi      |   Rp. 2000000   |")
  print("___________________________________________________")
listHargaTiket()
print(" ")

# DATA INPUT UNTUK PROGRAM PENJUALAN TIKET PESAWAT
namaKasir         = str(input("Masukan Nama Kasir               : "))
namaPelanggan     = str(input("Masukan Nama Pelanggan           : "))
tanggalTransaksi  = input("Masukan Tanggal Transaksi            : ")
nomerHp           = int(input("Masukan No. Handphone            : "))
kodeJurusan       = str(input("Masukan Kode Jurusan             : "))
jumlahTiket       = int(input("Masukan Jumlah Pembelian Tiket   : "))
uangBayar         = int(input("Masukan Uang Bayar               : "))
biayaAdmin        = 5000
pajakTiketPersen  = 0.1

# PROGRAM/SINTAKS PROGRAM PENJUALAN TIKET PESAWAT
if kodeJurusan == "MDN" or kodeJurusan == "mdn": 
    kotaTujuan = "Medan"
    hargaTiket = 2000000
elif kodeJurusan == "PDG" or kodeJurusan == "pdg": 
    kotaTujuan = "Padang"
    hargaTiket = 2200000
elif kodeJurusan == "SMG" or kodeJurusan == "smg": 
    kotaTujuan = "Semarang"
    hargaTiket = 1200000
elif kodeJurusan == "YGY" or kodeJurusan == "ygy": 
    kotaTujuan = "Yogyakarta"
    hargaTiket = 1500000
elif kodeJurusan == "JMB" or kodeJurusan == "jmb": 
    kotaTujuan = "Jambi"
    hargaTiket = 2000000
else: 
    print("Maaf, kode yang anda masukan salah")
    print("Silahkan masukan kode jurusan dengan benar")
    exit()

# MENGHITUNG SUBTOTAL, PAJAK, JUMLAH BAYAR, DAN UANG KEMBALIAN
subtotal = hargaTiket * jumlahTiket
pajakTiket = pajakTiketPersen * subtotal 
jumlahBayar = int(subtotal + pajakTiket + biayaAdmin)
uangKembalian = int(uangBayar - jumlahBayar)

# MENCETAK STRUK
header()
print(" ")
print(50*"-")
print("               TIKET GARUDA INDONESIA")
print(50*"-")
print(" ")
print("Nama Kasir              :", namaKasir)
print("Nama Pelanggan          :", namaPelanggan)
print("Tanggal Transaksi       :", tanggalTransaksi)
print("No. Handphone           :", nomerHp)
print("Kode Jurusan Pelanggan  :", kodeJurusan)
print("Kota Tujuan             :", kotaTujuan)
print("Harga Tiket        Rp.  :", hargaTiket)
print("Jumlah Pembelian Tiket  :", jumlahTiket)

print(5*"-", "DETAIL PEMBAYARAN", 5*"-")
print("Subtotal           Rp.  :", subtotal)
print("Ppn 10%            Rp.  :", pajakTiket)
print("Biaya Admin        Rp.  :", biayaAdmin)
print("                       _______ +")
print("Total Pembayaran   Rp.  :", jumlahBayar)
print("Tunai              Rp.  :", uangBayar)
print("                       _______ -")
print("Kembalian          Rp.  :", uangKembalian)
print(" ")
print("TERIMAKASIH")
