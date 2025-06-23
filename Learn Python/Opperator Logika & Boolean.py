# Beberapa operasi yang sering digunakan dalam logika dan boolean
# diantaranya adalah : not, or, and, xor

print('==== NOT ====')
a = True
c = not a

print('data a =',a)
print('----------- NOT')
print('data b =',c)

print('==== OR ====') # (Jika salah satu true maka hasilnya true)
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

print('==== AND ====') # (Jika salah satunya false maka akan false), jika keduanya true maka hasilnya true
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

a = False
b = True
c = a and b
print(a,'AND',b,'=',c)

a = True
b = False
c = a and b
print(a,'AND',b,'=',c)

a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

print('==== XOR ====') # Jika false ketemu false maka hasilnya false, sama juga dengan true hasilnya akan false
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)