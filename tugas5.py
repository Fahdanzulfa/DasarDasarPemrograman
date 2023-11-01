motor = ["Cbr150R","sport","150cc","merah","2"]
motor.append("Rp.35.300.000")
motor.append("tipe150cc")
motor.insert(2,"Honda")
print(motor)

print("""
       *** PILIH OPERASI ***
       1. HITUNG PERSEGI
       2. HITUNG LINGKARAN
       3. HITUNG SEGITIGA
      """)   

pilihan = input("Masukan Pilihan: ")
match pilihan:
    case "1":
        s = int(input("masukan sisi: "))
        persegi = s*s
        print('luas persegi', persegi)
    case "2":
        phi = 3.14
        r = int(input("masukan jari: "))
        lingkaran = phi*r*r
        print('luas lingkaran', lingkaran)
    case "3":
        l = 1/2
        a = int(input("masukan alas: "))
        t = int(input("masukan tinggi: "))
        segitiga = l*a*t
        print("luas segitiga", segitiga)
    case _:
        print("pilihan tidak tersedia")        