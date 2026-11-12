# Bab 1: Pengenalan & Instalasi Python
print("Halo, Python!")


print("Halo Python")



# Tipe data floating numbers
a = 7.5

print(a)


# Tipe data integers
x = 5
y = 3
z = 5 + 3

print(z)

# Tipe data floating numbers
a = 7.5

print(a)


# Menggunakan single quote
myFirstName = 'Rizqi'

# Menggunakan double quote
myLastName = "Maulana"

# Penulisan Angka sebagai string
myAge = "25"

# Penulisan string multiline
myHobby = """Hobi saya adalah
bersepeda dan bermain game.
"""

# Mencetak 2 variabel string dengan perintah print
print(myFirstName + " " + myLastName)
print("Umur saya " + myAge)


# Contoh penulisan boolean yang benar
a = True
b = False

# Contoh penulisan boolean yang salah
# Jika dijalankan, pada baris ini akan error
# c = true

# print(c)





a = 4
b = 2
# Penjumlahan
c = a + b
# Pengurangan
d = a - b
# Perkalian
e = a * b
# Pembagian
f = a / b
# Modulus
g = a % b
# Eksponensial
h = a ** b

# Cetak output
print(c) # 6
print(d) # 2
print(e) # 8
print(f) # 2
print(g) # 0
print(h) # 16


a = 3
b = 5
# Perbandingan sama dengan
c = a == b
# Perbandingan tidak sama dengan
d = a != b
# Perbandingan lebih kecil
e = a < b
# Perbandingan lebih kecil sama dengan
f = a <= b
# Perbandingan lebih besar
g = a > b
# Perbandingan lebih besar sama dengan
h = a >= b

# Cetak output
print(c) # False
print(d) # True
print(e) # True
print(f) # True
print(g) # False
print(h) # False


a = 3
b = 9

# Contoh Penggunaan "and"
print(a < 5 and b > 6) # True
print(a < 5 and b < 6) # False
print(a > 5 and b < 6) # False

# Contoh Penggunaan "or"
print(a < 5 or b > 6) # True
print(a < 5 or b < 6) # True
print(a > 5 or b < 6) # False

# Contoh Penggunaan "not"
print(not(a < 5 or b > 6)) # False
print(not(a > 5 or b < 6)) # True




# Bab 4: Kondisi If Else
nilai = 80

# If
if nilai >= 75:
    print("Lulus")

# If Else
if nilai >= 90:
    print("Sangat baik")
else:
    print("Cukup baik")

# If Elif Else
if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
else:
    print("Grade D")





# Bab 5: Perulangan

# For loop dengan range
for i in range(5):
    print("For loop ke-", i)

# For loop pada list
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print(item)

# While loop
angka = 1
while angka <= 5:
    print("While loop ke-", angka)
    angka += 1

# Break dan continue
for i in range(1, 8):
    if i == 3:
        continue
    if i == 6:
        break
    print(i)




# Bab 6: Lists dan Dictionaries

# List
buah = ["apel", "jeruk", "mangga"]
print(buah)
print(buah[0])

buah.append("pisang")
buah.remove("jeruk")
print(buah)
print(len(buah))

# Dictionary
siswa = {
    "nama": "Amanda",
    "kelas": "XI RPL",
    "umur": 16
}
print(siswa)
print(siswa["nama"])

siswa["jurusan"] = "RPL"
siswa["umur"] = 17
print(siswa)

# Perulangan pada dictionary
for key, value in siswa.items():
    print(key, ":", value)







# Bab 7: Function

# Function tanpa parameter
def sapa():
    print("Halo, selamat belajar Python!")

sapa()

# Function dengan parameter
def belajar_python(name, age):
    print("Halo, Saya %s. Umur saya %d" % (name, age))

belajar_python("Amanda", 16)

# Function dengan keyword arguments
belajar_python(age=17, name="Fika")

# Function dengan return value
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print(hasil)

# Function dengan arbitrary arguments
def sapa_semua(*names):
    for name in names:
        print("Halo,", name)

sapa_semua("Rizqi", "Fika", "Yudi")