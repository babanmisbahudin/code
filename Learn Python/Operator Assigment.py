# Apa itu Operator Assignment? operator yang dilakukan dengan penyingkatan, contoh dibawah :

a = 5 # adalah assigment biasa
print("Nilai a =", a)

# Contoh Operator Assignment Penyingkatan
# (Contoh +)
a = a + 1 # artinya a = a + 1
print("Nilai a + = 1, maka nilai a menjadi", a)
# (Contoh -)
a -= 2 # artinya a = a - 2
print("Nilai a - = 2, maka nilai a menjadi", a)
# (Contoh *)
a *= 5 # artinya a = a * 5
print("Nilai a * = 5, maka nilai a menjadi", a)
# (Contoh /)
a /= 2 # artinya a = a / 2
print("Nilai a / = 2, maka nilai a menjadi", a)

# Model Modulus (%)
b = 10
print("\nNilai b =", b)
b %= 3 # artinya b = b % 3
print("Nilai b % = 3, maka nilai b menjadi", b)

# Model Modulus (//) floor division
b = 10
print("\nNilai b =", b)
b //= 3 # artinya b = b // 3
print("Nilai b // = 3, maka nilai b menjadi", b)

#Model Aritmatika (Pangkat(**))
a = 5
print("\nNilai a =", a)
a **= 3 # artinya a = a ** 3
print("Nilai a ** = 3, maka nilai a menjadi", a)

# Model Bitwise (&, |, ^, ~, <<, >>)
# Model Bitwise OR (|)
c = True
print("\nNilai c =", c)
c |= False # artinya c = c | False
print("Nilai c | = False, maka nilai c menjadi", c)

c = False
print("\nNilai c =", c)
c |= False # artinya c = c | False
print("Nilai c | = False, maka nilai c menjadi", c)

# Model Bitwise AND (&)
c = True
print("\nNilai c =", c)
c &= False # artinya c = c & False
print("Nilai c & = False, maka nilai c menjadi", c)

c = True
print("\nNilai c =", c)
c &= True # artinya c = c & True
print("Nilai c & = True, maka nilai c menjadi", c)

# Model Bitwise XOR (^)
c = True
print("\nNilai c =", c)
c ^= False # artinya c = c ^ False
print("Nilai c ^ = False, maka nilai c menjadi", c)

c = True
print("\nNilai c =", c) 
c ^= True # artinya c = c ^ True
print("Nilai c ^ = True, maka nilai c menjadi", c)

# Model Binary

d = 0b0100
print("\nNilai d =", d, ", binary :", format(d, '04b'))

d >>= 2 # artinya d = d >> 2 (shifting right)
print("Nilai d >> = 2, maka nilai d menjadi", d, ", binary :", format(d, '04b'))

d <<= 1 # artinya d = d << 1 (shifting left)
print("Nilai d << = 1, maka nilai d menjadi", d, ", binary :", format(d, '04b'))