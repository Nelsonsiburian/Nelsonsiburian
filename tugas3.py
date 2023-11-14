string = ""
bar = 1

x = int(input("Masukkan angka :"))
no = x
# Looping Baris
while bar <= x:
	# Looping Kolom Spasi Kosong
	kol = bar	
	while kol > 1:
		string = string + "   "
		kol = kol - 1
	# Looping Kolom Angka Sisi Kanan
	kanan = 0
	while kanan <= (x - bar):
		string = string + " " + str(no) + " "
		kanan = kanan + 1	
		
	string = string + "\n"
	bar = bar + 1
	no = no - 1
print (string)