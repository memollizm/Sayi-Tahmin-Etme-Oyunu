import random

print("************** Sayı Tahmin Etme Oyunu **************")

sayi = random.randint(1,100)
can = int(input("Kaç adımda tahmin edebilirsin ?: "))
hakSayisi = can
sayac = 0
puan = 100

while hakSayisi > 0:
    hakSayisi -= 1
    sayac += 1
    tahmin = int(input("Tahmininiz: "))

    if sayi == tahmin:
        print("Tebrikler bildiniz. ",sayac,". adımda bildiniz")
        print(f'Toplam puanınız: {100 - (100/can) * (sayac-1)}')
        break
    elif sayi > tahmin:
        print("Yukarıda bir tahminde bulununuz.")
    else:
        print("Aşağıda bir tahminde bulununuz.")

    if hakSayisi == 0:
        print("Tüm haklarınızı kullandınız. Tutulan sayı: ",sayi)