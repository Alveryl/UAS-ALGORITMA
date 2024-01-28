#Tugas Aplikasi Kasir


print("--------- BAR - BAR ---------") #Nama RESTORAN
print("BARBAR KUY")

#Penginputan Pembeli untuk pesan makanan

pembeli = input("Masukkan nama Pembeli: ") #ALVERYL
alamat = input("Masukkan alamat rumah Pembeli: ") #Jl SETIA
No_telp = int(input("Masukkan No. Telepon Pembeli: ")) #089652487960

#memberikan informasi waktu real-time dan informasi pembeli

import time
hari_ini = time.asctime( time.localtime(time.time()) )
data = pembeli + "di" + alamat + "dengan nomer telepon:"  
print ("Pesanan atas nama :", pembeli) 

#List sebuah menu 
def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n------- FOOD List -------")
   print("1. AYAM GORENG - Rp 6.000")
   print("2. AYAM BAKAR - Rp 8.000")
   print("3. IKAN GORENG - Rp 10.000")
   print("4. IKAN BAKAR - Rp 12.000")
   print("5. SPESIAL BARBAR - Rp 15.000")
   nomor=int(input("Masukan Pilihan: "))#2
   porsi= int(input("Berapa Porsi: "))#3

   #Percabangan untuk membuat hasil dari program
   
   if nomor==1:
       totalmkn=porsi*6000
       print (porsi," porsi AYAM GORENG = Rp", totalmkn)
       mkn=("AYAM GORENG")
   elif nomor==2:
       totalmkn=porsi*8000
       print (porsi," AYAM BAKAR = Rp", totalmkn)
       mkn=("AYAM BAKAR")
   elif nomor==3:
       totalmkn=porsi*10000
       print (porsi, " porsi IKAN GORENG = Rp", totalmkn)
       mkn=("IKAN GORENG")
   elif nomor==4:
       totalmkn=porsi*12000
       print (porsi," porsi IKAN BAKAR = Rp", totalmkn)
       mkn=("IKAN BAKAR")
   elif nomor==5:
       totalmkn=porsi*15000
       print (porsi," porsi SPESIAL BARBAR = Rp", totalmkn)
       mkn=("SPESIAL BARBAR")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

#List input Menu minuman

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----- DRINK List -----")
   print("1. AIR PUTIH - Rp 6.000")
   print("2. ES T - Rp 8.000")
   print("3. ES U - Rp 10.000")
   print("4. ES V - Rp 15.000")
   print("5. MINUM BARBAR - Rp 15.000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

#Percabangan untuk membuat hasil dari menu minuman
   if nomor==1:
       totalmnm=gelas*6000
       print (gelas," Botol AIR PUTIH = Rp", totalmnm)
       mnm=(" Botol AIR PUTIH")
   elif nomor==2:
       totalmnm=gelas*8000
       print (gelas, " Gelas ES T = Rp", totalmnm)
       mnm=("ES T")
   elif nomor==3:
       totalmnm=gelas*10000
       print (gelas, " Gelas ES U = Rp", totalmnm)
       mnm=("ES U")
   elif nomor==4:
       totalmnm=gelas*15000
       print (gelas," Gelas ES V = Rp", totalmnm)
       mnm=("ES V")
   elif nomor==5:
       totalmnm=gelas*15000
       print(gelas," Gelas MINUM BARBAR = Rp", totalmnm)
       mnm=("MINUM BARBAR")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

#hasil dari total harga dari makanan dan minuman
fungsimakanan()
fungsiminuman()         
totalsemua=totalmkn+totalmnm


#visualisasi struk dari hasil pemesanan

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))#40000
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("======= S T R U K   B E L I =======")
print("====================================")
print ("Nama\t\t\t:",pembeli)
print ("Alamat\t\t\t:", alamat)
print ("Nomor Telepon\t\t:", "+62",No_telp)
print ("Beli\t\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Total\t\t\t: Rp",totalsemua)
print ("Dibayar\t\t\t: Rp",uang)
print ("Kembalian\t\t: Rp",kembalian)
print ("Tanggal pembelian\t:", hari_ini)
print("==================================")
print("==================================")
