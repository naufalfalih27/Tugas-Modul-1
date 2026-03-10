def isKabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

tahun_input = int(input("Masukkan tahun: "))

if isKabisat(tahun_input):
    print("Hasil: Tahun Kabisat")
else:
    print("Hasil: Bukan Tahun Kabisat")