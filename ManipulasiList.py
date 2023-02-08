## Operasi

#Index  0(-4)   1(-3)   2(-2)   1(-1)  
data = ["Bang","Dzaki","Ganteng","Banged"]

# Mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"Data terakhir adalah = {data_terakhir}")

data_bang = data[-4]
print(f"Data Bang = {data_bang}")

# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"Panjang data adalah {panjang_data}")

## Manipulasi data list (Merubah data listnya)

# Menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")
data.insert(0,"Alif")
print(f"data sesudah ditambah = \n{data}")

# Menambah data di akhir
data.append("Bambang")
print(f"data ditambah lagi =\n{data}")

# Menambah list dengan list
data_baru = ["Farras","Fatih","Fikri"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

# Merubah data
# kita ubah data ke 2 menjadi Difa
data[2] ="Difa"
print(f"data rubah = {data}")

# Menghapus data Bang
data.remove("Bang")
print(f"data remove = \n{data}")

# Menghapus data paling belakang
data.pop()
print(f"data akhir = \n{data}")