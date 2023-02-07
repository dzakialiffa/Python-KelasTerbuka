# Operasi dan manipulasi string
# 1. Menyambung string (concatenate)
print("===MENYAMBUNG STRING===")
nama_pertama = "Dzaki"
nama_tengah = "Merupakan"
nama_akhir = "Nama Saya"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang dari string
print("===HITUNG PANJANG DARI STRING===")
panjang = len(nama_lengkap)
print("panjang dari" + " " + nama_lengkap + " = " + str (panjang)) # Spasih dihitung

#3. Operator untuk string

# Mengecek apakah ada komponen char atau string di string
print("===CEK CHAR ADA DI STRING===")
d = "d"
status = d in nama_lengkap
print("string" + " " + d + " " + "ada di" + " " + nama_lengkap +"=" + str(status))

# Mengecek apakah tidak ada komponen char atau string di string
print("===CEK CHAR TIDAK ADA DI STRING===")
d = "d"
status = d not in nama_lengkap
print("string" + " " + d + " " + "tidak ada di" + " " + nama_lengkap +"=" + str(status))

# Mengulang string
print("===MENGULANG STRING===")
print("wk"*10)
print(10*"wk")

# Indexing
print("===INDEXING===")
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-7 : " + nama_lengkap[7])

# Item Paling Kecil
print("===ITEM PALING KECIL===")
print("paling kecil : " + min(nama_lengkap))
# Item Paling Besar
print("===ITEM PALING BESAR===")
print("paling kecil : " + max(nama_lengkap))

# 4. Operator dalam bentuk method
print("===OPERATOR DALAM BENTUK METHOD===")
data ="Nama saya Dzaki"
jumlah = data.count("a")
print("Jumlah a pada"+ data + "=" + str(jumlah))

## Merubah case dari string
print("===MERUBAH CASE KE UPPER===")
salam = "bro!"
print("normal =" + salam)
salam = salam.upper()
print("upper =" + salam)

# merubah semua ke lower case
print("===MERUBAH CASE KE LOWER===")
salam = "bro!"
print("normal =" + salam)
salam = salam.lower()
print("lower =" + salam)

# Pengecekkan dengan isX Method
print("===PENGECEKKAN DENGAN ISX METHOD===")
salam = "sist!"
apakah_lower = salam.islower() # hasilnya bool
print(salam + "is lower =" + str(apakah_lower))
apakah_upper = salam.isupper() 
print(salam + "is upper =" + str(apakah_upper))

judul = "Aku adalah anak baik"
cek_judul = judul.istitle()

print(judul + "is title =" + str(cek_judul))

## Cek komponen starwith() endswith() <----- keren
print("===CEK KOMPONEN STARWITH, ENDSWITH===")
cek_start = "Anyeong Dzaki".startswith("anyeong")
print("start =" + str(cek_start))

cek_end = "Anyeong Dzaki".endswith("dzakis")
print("end =" + str(cek_end))

# Penggabungan komponen join() split()
print("===PENGGABUNGAN KOMPONEN JOIN, SPLIT===")
pisah = ['Aku', 'Sayang', 'Kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = 'ehm'.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# Alokasi karakter rjust(), ljust(), center()
print("===ALOKASI KARAKTER RJUST, LJUST, DAN CENTER===")
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,":")
print("'"+tengah+"'")

# Kebalikannya -> strip()
print("===KEBALIKAN MENGGUNAKAN STRIP===")
tengah = tengah.strip(":") # Menghilangkan tanda :
