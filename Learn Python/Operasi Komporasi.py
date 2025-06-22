# Setiap hasil dari komparasi adalah boolean yaitu True atau False
# Contoh Operator Komparasi > , <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih besar dari >
print("------- Lebih besar dari > -------")
hasil = a > 3
print(a, '>', 3, "=", hasil)

hasil = b > 3
print(b, '>', 3, "=", hasil)

hasil = b > 2
print(b, '>', 2, "=", hasil)

# Kurang dari <
print("------- Kurang dari < -------")
hasil = a < 3
print(a, '<', 3, "=", hasil)

hasil = b < 3
print(b, '<', 3, "=", hasil)

hasil = b < 2
print(b, '<', 2, "=", hasil)

# Lebih besar atau sama dengan >=
print("------- Lebih besar atau sama dengan >= -------")
hasil = a >= 3
print(a, '>=', 3, "=", hasil)

hasil = b >= 3
print(b, '>=', 3, "=", hasil)

hasil = b >= 2
print(b, '>=', 2, "=", hasil)

# Kurang dari sama dengan <=
print("------- Kurang dari sama dengan <= -------")
hasil = a <= 3
print(a, '<=', 3, "=", hasil)

hasil = b <= 3
print(b, '<=', 3, "=", hasil)

hasil = b <= 2
print(b, '<=', 2, "=", hasil)

# Sama dengan ==
print("------- Sama dengan == -------")
hasil = a == 3
print(a, '==', 3, "=", hasil)

hasil = b == 3
print(b, '==', 3, "=", hasil)

hasil = b == 2
print(b, '==', 2, "=", hasil)

# Tidak sama dengan !=
print("------- Tidak sama dengan != -------")
hasil = a != 3
print(a, '!=', 3, "=", hasil)

hasil = b != 3
print(b, '!=', 3, "=", hasil)

hasil = b != 2
print(b, '!=', 2, "=", hasil)

# Is sebagai komparasi object identitas
x = 5 # ini adalah assignment membuat object
y = 5 # ini adalah assignment membuat object
print('nilai x:',x, '.id =', hex(id(x)))
print('nilai y:',y, '.id =', hex(id(y)))

hasil = x is y
print('x is y =', hasil)

# Is not sebagai komparasi object identitas
x = 6 # ini adalah assignment membuat object
y = 5 # ini adalah assignment membuat object
print('nilai x:',x, '.id =', hex(id(x)))
print('nilai y:',y, '.id =', hex(id(y)))

hasil = x is y
print('x is y =', hasil)
