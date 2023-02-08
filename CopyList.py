## Teknik Menduplikasi List

a = ["Alif","fikri","dzaki"]
print(f"a = {a}")

b = a 
print(f"b = {b}")

# Kita akan merubah member dari a

a[1] = "dzaki"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# Address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# Menduplikasi list dengan copy
print("Membuat list C dengan a.copy")
c =a.copy()

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"a = {c}")

print("Kita ubah data 1")
c[1] = "HAH"

print(f"a = {a}")
print(f"b = {b}")
print(f"a = {c}")