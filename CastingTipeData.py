# Casting Merubah Tipe Data ke Tipe Data Lainnya
# Tipe data = int, float, str, bool

## Integer
print("====INTEGER====")
data_integer = 9
print("data =", data_integer, ",type =", type(data_integer))

data_float = float(data_integer)
print("data =", data_float, ",type =", type(data_float))

data_string = str(data_integer)
print("data =", data_string,",type =", type(data_string))

data_boolean = bool(data_integer)
print("data =", data_boolean,",type =",type(data_boolean)) # Akan false jika nilai 0

## Float
print("====FLOAT====")
data_float = 9.5
print("data =", data_float, ",type =", type(data_float))

data_integer = int(data_float)
print("data =", data_integer, ",type =", type(data_integer))

data_string = str(data_float)
print("data =", data_string,",type =", type(data_string))

data_boolean = bool(data_float)
print("data =", data_boolean,",type =",type(data_boolean)) # Akan false jika nilai 0

## Boolean
print("====BOOLEAN====")
data_boolean = False
print("data =", data_boolean, ",type =", type(data_boolean))

data_integer = int(data_boolean)
print("data =", data_integer, ",type =", type(data_integer))

data_string = str(data_boolean)
print("data =", data_string,",type =", type(data_string))

data_boolean = float(data_boolean)
print("data =", data_boolean,",type =",type(data_float))

## String
print("====STRING====")
data_string = "10";
print("data =", data_string, ",type =", type(data_string))

data_integer = int(data_string)
print("data =", data_integer, ",type =", type(data_integer))

data_float = str(data_string)
print("data =", data_float,",type =", type(data_float))

data_boolean = float(data_string)
print("data =", data_boolean,",type =",type(data_float))