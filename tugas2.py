string = ""

x = int(input("Masukkan angka :"))
bar = x
no = 0
# Looping Baris
while bar >= 0:
	# Looping Kolom Spasi Kosong
	kol = bar
	while kol > 0:
		string = string + "   "
		kol = kol - 1
	# Looping Kolom Angka Sisi Kanan
	kanan = 1
	while kanan < (x - (bar-1)):
		string = string + " " + str(no) + " "
		kanan = kanan + 1		
		
	string = string + "\n"
	bar = bar - 1
	no = no + 1
print (string)