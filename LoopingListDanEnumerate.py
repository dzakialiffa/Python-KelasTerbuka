# Looping dari list

# For Loop
print("For Loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["Dzaki","Aliffa","Farras"]

for nama in peserta:
    print(f"nama = {nama}")

# For Loop dan Range
print(f"For Loop dan Range")
kumpulan_angka = [10,5,4,2,6]

panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"Angka = {kumpulan_angka[i]}")

# While
print(f"While Loop")
kumpulan_angka = [10,5,4,2,6]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# List comprehension
print("List Comprehension")
data = ["Dzaki",1,2,3,4,5,5]
[print(f"data={i}") for i in data]

angka = [22,33,11,44,22]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# Enumerate
print("Enumerate")
data_list = ["Dzaki",1,2,3,4,5,6]

for index, data in enumerate(data_list):
    print(f"index = {index}, data ={data}")