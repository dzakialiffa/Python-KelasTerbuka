# Operator Dictionary

data_dict = {
    'Dzaki': "Iya Gue Dzaki",
    'Fikri': "Iya Ini Nama Tengah Gue",
    'Aliffa': "Ini nama akhir gue oi"
}

# Panjang Dictionary
LENDICT = len(data_dict)
print(f"Panjang Dictionary Adalah {LENDICT}")

# Mendetek Key itu ada atau tidak
KEY = "Dzaki"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict: {CHECKKEY}")

# Mengakses Value dengan GET
print(data_dict["Dzaki"])
print(data_dict.get("Dzaki"))
print(data_dict.get("Dzak", "KEY tidak ditemukan"))

# Mengupdate Data
data_dict["Dzaki"] = "Dzaki si ganteng"
print(data_dict)
data_dict["Aliffa"] = "Alif si Ganteng"
print(data_dict)

data_dict.update({"Dzaki":"Aku Ganteng banget anjay"})
print(data_dict)
data_dict.update({"Faqih":"Faqih si faqih"})
print(data_dict)

# Mendelete data dari dictionary
del data_dict["Faqih"]
print(data_dict)