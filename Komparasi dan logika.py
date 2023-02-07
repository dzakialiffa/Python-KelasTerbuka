# Membuat gabungan area rentang dari angka

#++++++3-----------10++++++++
inputUser = float(input("Masukkan angka yang bernilai"))

# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print(isKurangDari)

#------------10++++++++++
#Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan: ", isCorrect)

#-----------3++++++++++10-----------
# kasus irisan

inputUser = float(input("Masukkan angka yang bernilai bagus"))