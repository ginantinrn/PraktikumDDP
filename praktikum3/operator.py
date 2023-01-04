while True:
    number = int(input("masukan angka: "))
    if number == 0:
        break

    if number % 2 == 0:
        print ("Bilangan Genap")
    else:
        print("Bilangan Ganjil")