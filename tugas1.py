string = ""

bar = int(input("Masukkan angka :"))
no = bar
# Looping Baris
while bar >= 0:
	# Looping Kolom
	kol = bar
	while kol > 0:
		string = string + " " + str(no) + " "
		kol = kol - 1
		
	string = string + "\n"
	bar = bar - 1
	no = no - 1
print (string)
