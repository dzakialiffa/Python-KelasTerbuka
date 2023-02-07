# a = 10, a adalah variabel dengan nilai 10

# tipe data: Angka satuan (integer)
data_integer = 1 # di python tidak ada int
print("data : ", data_integer) 
print("-bertipe :", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.1
print("data : ", data_float)
print("-bertipe :", type(data_float))

# tipe data: angka dengan koma (string)
data_string = "Dzaki"
print("data : ", data_string)
print("-bertipe :", type(data_string))

# tipe data: angka dengan koma (boolean)
data_bool = True
print("data : ", data_bool)
print("-bertipe :", type(data_bool))

## tipe data khusus

# tipe data kompleks
data_complex = complex(11,2)
print("data : ", data_complex)
print("-bertipe :", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double (11.02)
print("data :", data_c_double)
print("-bertipe : ", type(data_c_double))