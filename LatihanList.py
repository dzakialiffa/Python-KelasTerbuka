# Program List Buku

list_buku = []
while True:
    print("\nMasukkan Data Buku")
    judul = input("Judul Buku\t\t: ")
    penulis = input("Nama Penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n\n","="*20)
    isLanjut = input("Lanjut Gak?(y/n)")

    if isLanjut == "n":
        break

print("UDAHAN")
