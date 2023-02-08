# Membuat segitiga dengan perulangan

sisi = 10

# 1. Menggunakan For
#dummy variable
print("Awal Dari For")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
print("Akhir dari For")

# 2. Menggunakan while
print("Awal dari While")
count = 1 
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break
print("Akhir dari While")

# 3. Hanya Ganjil Saja
print("Awal dari While")
count = 1 
while True:
    # Akan kembali ke atas jika ganjil
    if (count%2):
        # Print jika ganjil
        print("*"*count)
        count += 1
    else:
        count += 1
        continue
    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("Akhir dari While")