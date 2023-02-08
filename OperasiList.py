data_angka = [1,2,3,4,5,6,7,8,9,0]

print(f"data angka = \n{data_angka}")

#count
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"Jumlah angka 4 = {jumlah_data_4}")
print(f"Jumlah angka 3 = {jumlah_data_3}")

# Ambil posisi data
data = ["dzaki","fikri","aliffa","moch"]
print(f"data={data}")

index_dzaki = data.index("dzaki")
print(f"index si dzaki = {index_dzaki}")

# Mengurutkan list
print(f"data angka sebelum sort \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# Balik list
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n {data}")