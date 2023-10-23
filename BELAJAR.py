bil1 = int(input("masukan bilangan 1: "))
bil2 = int(input("masukan bilangan 2: "))
operator = input("masukan operator :")
if (operator == "+"):
  hasil = bil1 + bil2
  print("hasil penjumlahan =", hasil)
elif (operator == "-"):
  hasil = bil1 - bil2
  print("hasil pengurangan =", hasil)
elif (operator == "/"):
  hasil = bil1 / bil2
  print("hasil pembagian =", hasil)
elif (operator == "*"):
  hasil = bil1 * bil2
  print("hasil perkalian =", hasil)
elif (operator == "**"):
  hasil = bil1 ** bil2
  print("hasil perpangkatan =", hasil)
else:
  print("maaf operator yang anda masukan salah")
  