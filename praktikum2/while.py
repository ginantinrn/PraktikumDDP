# angka = 1

# while angka > 0 and angka < 11 :
#     angka = int (input("masukan bilangan bulat: "))
#     if angka >= 1:
#         print("bilangan positif")
#     elif angka < 0: 
#         print("bilangan negatif")
#     else:
#         print("bilangan nol")

while True:
    nama = input("masukan nama anda: ")
    if nama == "x":
        break
    elif nama == "jeno":
        continue
    print("selamat datang ", nama)