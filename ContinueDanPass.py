# Pass berfungsi sebagai dummy jadi tidak akan dieksekusi

# angka = 0

# while angka < 5:
#     angka += 1
#     if angka == 3:
#         print("anjayy!")
#         pass # ini gakan dieksekusi
#     print(angka)

# Continue

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if angka == 3:
     print("nice")
     continue # akan membuat loop meloncat

    print("wharsap") # aksi 2 
    
print("pinish")