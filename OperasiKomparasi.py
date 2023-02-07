# Operasi komarasi adalah untuk membandingkan nilai
# setiap hasil dari operasi komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print('===== lebih besar dari (>)====')
hasil = a > 3
print (a,'>',3,'=',hasil)
hasil = b > 3
print (b,'>',3,'=',hasil)
hasil = b > 2
print (b,'>',2,'=',hasil) # hasilnya false tapi kalo 2.1 maka besar 2.1

# Kurang dari <
print('===== kurang dari (>)====')
hasil = a < 3
print (a,'<',3,'=',hasil)
hasil = b < 3
print (b,'<',3,'=',hasil)
hasil = b < 2
print (b,'<',2,'=',hasil)

# lebih dari sama dengan (>=)
print('==== Lebih Dari Sama Dengan (>=)====')
hasil = a >=  3
print (a,'>=',3,'=',hasil)
hasil = b >= 3
print (b,'>=',3,'=',hasil)
hasil = b >= 2
print (b,'>=',2,'=',hasil)

# kurang dari sama dengan (<=)
print('==== Kurang Dari Sama Dengan (<=)====')
hasil = a <= 3
print (a,'<=',3,'=',hasil)
hasil = b <= 3
print (b,'<=',3,'=',hasil)
hasil = b <= 2
print (b,'<=',2,'=',hasil)

# sama dengan (==)
print('==== Sama Dengan (==)====')
hasil = a == 3
print (a,'==',3,'=',hasil)
hasil = b == 3
print (b,'==',3,'=',hasil)
hasil = b == 2
print (b,'==',2,'=',hasil)

# tidak sama dengan (!=)
print('==== Tidak Sama Dengan (!=)====')
hasil = a != 3
print (a,'!=',3,'=',hasil)
hasil = b != 3
print (b,'!=',3,'=',hasil)
hasil = b != 2
print (b,'!=',2,'=',hasil)

print("==== Object Identity(Is Not)")
# 'is' sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is 5 =', hasil)

x = 5
y = 6
print('nilai x =',x,',id = ', hex(id(x)))
print('nilai x =',y,',id = ', hex(id(y)))
hasil = x is not y
print('x is y =', hasil)