#Casting adalah merubah tipe data dari satu tipe ke tipe data lain.

#Data Interger
print("============= Interger ============")
data_int = 5;#akan false jika data_int = 0
print("data = ", data_int, ", type =", type(data_int))

data_float = float(data_int)  # Mengubah integer ke float
data_str =str(data_int)  # Mengubah integer ke string
data_bool = bool(data_int)  # Mengubah integer ke boolean

print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_bool, ", type =", type(data_bool))

# Data Float
print("============= Float ============")
data_float = 5.5;
print("data = ",data_float, ",type =", type(data_float))

data_int = int(data_float)
data_str = str(data_float) 
data_bool = bool(data_float)  

print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_bool, ", type =", type(data_bool))

# Data Boolean
print("============= Boolean ============")
data_float = True
print("data = ",data_bool, ",type =", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool) 
data_float = float(data_bool)  

print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_float, ", type =", type(data_float))

# Data String
print("============= String ============")
data_str = "10"
print("data = ",data_str, ",type =", type(data_str))

data_int = int(data_str)
data_float = float(data_str)  
data_bool = bool(data_str) 

print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_bool, ", type =", type(data_bool))