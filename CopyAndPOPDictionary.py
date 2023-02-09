
buah_buah = {
    "nanas":"haseum pisan",
    "apel":"enak pisan",
    "anggur":"enak sih"
}

buah = buah_buah.copy()
print(f"buah-buah: {buah_buah}\n")
print(f"Buah: {buah}\n")

buah_buah["nanas"]="Nanas si paling enak"
print(f"buah-buah: {buah_buah}\n")
print(f"Buah: {buah}\n")

# Mau ngambil data ini dan keluar dari buah
# Pop dictionary
dataApel = buah.pop("apel")
print(f"Data Apel = {dataApel}\n")
print(f"Buah = {buah}")

