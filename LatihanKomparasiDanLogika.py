# Latihan Komparasi dan Logika

# Kasus Gabungan
print("===Kasus Gabungan===")
inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10"))
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =",isKurangDari)
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =",isLebihDari)
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan ", isCorrect)

# Kasus Irisan
print("===Kasus Irisan===")
print("\n",10*"=","\n")
inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 3 \ndan \nlebih besar dari 10"))
# Memeriksa Angka Lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 =", isLebihDari)
# Memeriksa Angka Kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10", isKurangDari)
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan ", isCorrect)