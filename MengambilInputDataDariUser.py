# Input User

# Data yang dimasukkan pasti string
data = input("Masukkan data: ")

print("data = ", data,"type =", type(data))

# Jika ingin mengambil int, maka
angka = float(input("masukkan angka: "))
angka = int(input("Masukkan angka: "))

print("data =", angka,",type =", type(angka))

# Jika ingin mengambil boolean, maka
print("data =", angka,",type =", type(angka))
biner = bool(int(input("Masukkan nilai boolean: "))) # Mengkonversikan data string ke integer terus ke boolean

print("data= ", biner,",type =", type(biner))