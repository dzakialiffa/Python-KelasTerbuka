## LIST

# Kumpulan data numbers
data_angka = [1,2,3,4,5,6,7]
print(data_angka)

# Kumpulan data string
data_string = ["aku","Sayang","Kamu","Ki"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, False, True]
print(data_boolean)

# Kumpulan data campuran
data_campuran = ["Beli",5,"Bala-bala",True]
print(data_campuran)

# Cara alternatif membuat list
data_range = range(0,10,2) #start, stop, step
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list dengan for loop
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)

# Membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i !=5]
print(list_pake_for_if)

list_pake_for_if_genap = [i for i in range(0,10) if i %2 ==0]
print(list_pake_for_if_genap)

list_pake_for_if_ganjil = [i for i in range(0,10) if i %2 !=0]
print(list_pake_for_if_ganjil)
