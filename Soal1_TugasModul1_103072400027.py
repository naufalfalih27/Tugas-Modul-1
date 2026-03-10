def isKabisat(tahun):
    #Syarat kabisat: habis dibagi 4 DAN tidak habis dibagi 100, ATAU habis dibagi 400
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True # Mengembalikan nilai True jika syarat terpenuhi
    else:
        return False # Mengembalikan nilai False jika syarat tidak terpenuhi

tahun_input = int(input("Masukkan tahun: "))

if isKabisat(tahun_input):
    print("Hasil: Tahun Kabisat")
else:
    print("Hasil: Bukan Tahun Kabisat")