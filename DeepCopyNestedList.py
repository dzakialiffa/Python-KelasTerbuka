data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0, data_1]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# Mengambil data dari nested list

data = data_2D[1][0]
print(f"data = {data}")

# address semuanya

print(f"address data_2D = {hex(id(data_2D))}")
print(f"address data_2D copy = {hex(id(data_2D_copy))}")

print("address dari member ke-1")
print(f"address data_2D = {hex(id(data_2D[0]))}")
print(f"address data_2D copy = {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5
data_2D

# Deep Copy
from copy import deepcopy

data_2D = [data_0, data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D))}")
print(f"address deep = {hex(id(data_2D_deepcopy))}")

print("address dari member ke-1")
print(f"address data_2D = {hex(id(data_2D[0]))}")
print(f"address data_2D copy = {hex(id(data_2D_deepcopy[0]))}")