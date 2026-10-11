f = 1
f = f+1
while f < 1000:
    islem = int(input("Toplama için 1'e, çıkarma için 2'ye basın: "))

    if islem == 1:
        a = int(input("Birinci sayıyı gir: "))
        b = int(input("İkinci sayıyı gir: "))
        print("Toplam:", a + b)

    elif islem == 2:
        c = int(input("Birinci sayıyı gir: "))
        d = int(input("İkinci sayıyı gir: "))
        print("Fark:", c - d)


 