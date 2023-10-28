rows = int(input("masukan jumlah baris: "))
for i in range(rows, 0, -1):
    for j in range(1, i+1):
      print(j, end=" ")
    print()


string = " "
bar = 1

x = int(input("masukan angka :"))
print("\n")
#looping bari
while bar <= x:
       kol = bar
       # looping kolom spasi kosong
       while kol > 1:
         string = string + "  "
         kol = kol - 1
         # looping kolom bintang sisi kiri
         kiri = 0
         while kiri <= (x - bar):
           string = string + " * "
           kiri = kiri + 1
           # looping kolom bintang sisi kanan
           kanan = kiri
           while kanan > 1:
             string = string + " * "
             kanan = kanan - 1
             
         string= string + "\n\n"
         bar = bar + 1
print(string)
             
   