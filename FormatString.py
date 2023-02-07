# format string

# Contoh generic
# String
nama = "Dzaki"
format_str = f"Hello {nama}"
print(format_str)

# Boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# Angka
angka = 2001.2
format_str = f"Angka = {angka}"
print(format_str)

# Bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# Bilangan dengan ordo ribuan
angka = 2023
format_str = f"ribuan = {angka:,}"
print(format_str)

# Bilangan desimal
angka = 2001.2345
format_str = f"desimal = {angka:.2f}"
print(format_str)

# Menampilkan leading zero
angka = 2001.2345
format_str = f"desimal = {angka:9.2f}"
print(format_str)

# Menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus {angka_plus:+d}"

print(format_minus)
print(format_plus)

# Memformat Persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# Melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga*jumlah}"
print(format_string)

# Format angka lain (binary, ocal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)