# Latihan Percabangan (Pembuatan Kalkulator)

print(10*"=")
print("kalkulator Sederhana")
print(10*"=" + "\n")

angka_1 = float(input("Masukkan angka 1 ="))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("Masukkan angka 2 ="))

# Percabangannya
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
else :
    print("Masukkan yang bener dong!, aku pusing")
print("Akhir dari program, terima gajih!")