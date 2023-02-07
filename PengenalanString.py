data = " ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string
'''
1. Menggunqkqn single quote
2. Menggunakan double quote
'''

print('Halo apa kabar, nama saya Dzaki') # Menggunakan single quote
print("Halo apa kabar, nama saya Dzaki") # Menggunakan double quote

# 2. Menggunakan tanda \
# Membuat tanda ' menjadi string
print('Masi shalat jum\'at')
print('g\'day, isn\'t it?')

# backslah
print("C:\\user\\dzaki")

# tab
print ("Dzaki \t\t\t lagi jauhan wkwk")

# backspace
print("Dzaki \bGanteng, jadi deketan")

# newLine
print("baris pertama \n baris kedua.") # LF
print("baris pertama. \rbaris kedua") # CR
print("baris pertama. \r\nbaris kedua") # CRLF

# 3. String literal raw
print('C:\new folder') # Akan salah path nya

# Menggunakan raw string
print(r'C:\new folder')

# Multiline literal string
print("""
Nama : Dzaki
Kelas : 12
""")

# Multiline literal string dan RAW
print(r"""
Nama: Dzaki
Kelas: 12 
website: www.dzaki.com/ID
""")