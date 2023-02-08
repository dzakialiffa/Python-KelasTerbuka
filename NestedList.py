data_0 = [1,2]
data_1 = [3,4]

data_listLbiasa = [1,2,3,4]

print(f"List biasa = {data_listLbiasa}")

list_2D = [data_0,data_1]
print(f"List 2D = {list_2D}")

# Contoh penggunaan

peserta_0 = ["Dzaki", 22, "Laki-laki"]
peserta_1 = ["Fikri", 21, "Laki-laki"]
peserta_2 = ["Fany", 19, "Perempuan"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"Peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")

# Dengan reference

list_copy = list_peserta.copy()
print(f"peserta = {list_copy}")
peserta_0[0] = "DEON"
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")