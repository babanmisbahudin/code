a = 10
b = 3

# Oprasi Penambahan +
hasil = a + b
print("OPERASI PENAMBAHAN ---",a,'+',b,'=',hasil)

# Oprasi Pengurangan -
hasil = a - b
print("OPERASI PENGURANGAN ---",a,'-',b,'=',hasil)

# Oprasi Perkalian *
hasil = a * b
print("OPERASI PERKALIAN ---",a,'*',b,'=',hasil)

# Oprasi Perbagian /
hasil = a / b
print("OPERASI PEMBAGIAN ---",a,'/',b,'=',hasil)

# Oprasi Eksponen (Pangkat) **
hasil = a ** b
print("OPERASI EKSPONEN ---",a,'**',b,'=',hasil)

# Oprasi Modulus (sisa pembagian) %
hasil = a % b
print("OPERASI MODULUS ---",a,'%',b,'=',hasil)

# Operasi Floor Devision //
hasil = a // b
print("OPERASI FLOOR DEVISIOM ---",a,'//',b,'=',hasil)

'''
    1. ()
    2. exponen **
    3. perkalian & teman-teman * / ** % //
    4. penambahan dan pengurangan + -
'''

# Prioritas Operasi, Operational Precedence
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print ("OPERASI PRECEDENCE ---",x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

# Contoh lainnya
hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

# Kurang akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(',x,'+',y,')*',z,'=',hasil)
