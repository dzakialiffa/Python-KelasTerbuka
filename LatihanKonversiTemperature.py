print ("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("Suhu adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ", reamur, "Reamur")

# fahrenheit
fahrenheit = 9/5 * celcius + 32
print(" suhu dalam faherenheit adalah ", fahrenheit, "fahrenheit")

# Kelvin
kelvin = celcius + 273
print(" suhu dalam kelvin adalah ", kelvin, "kelvin")
