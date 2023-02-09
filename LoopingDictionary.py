# Looping Dictionary
buah = {
    "Apel":"Apel surapel",
    "Nanas":"Nanas Haseum"
}

# Looping first try (yang keluar adalah KEY
for buahh in buah:
    print(buahh)

# Operator untuk mengambil item / iterables
keys = buah.keys()
print(keys)

for key in buah.keys():
    print(buah.get(key))
values = buah.values()
print(values)

for value in buah.values():
    print(value)

items = buah.items()
print(items)

for item in buah.items():
    print(item)

for key, value in buah.items():
    print(f"key = {key}, value = {value}")
