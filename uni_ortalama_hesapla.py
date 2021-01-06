krediler = []
ders_adlari = []
ders_harfleri = []
krediler_toplami = []

harf_karsiliklari = {
    "AA" : 4.00,
    "AB" : 3.75,
    "BA" : 3.33,
    "BB" : 3.00,
    "BC" : 2.75,
    "CB" : 2.33,
    "CC" : 2.00,
    "CD" : 1.75,
    "DC" : 1.33,
    "DD" : 1.00,
    "FF" : 0.00
}

ders_sayisi = int(input("ders sayısı : "))

for i in range(ders_sayisi):

    ders_adi = input("ders adi : ")
    ders_kredi = int(input("ders kredi : "))
    ders_harf = input("ders harf : ")

    krediler.append(ders_kredi)
    ders_adlari.append(ders_adi)
    ders_harfleri.append(ders_harf)

    krediler_toplami.append(harf_karsiliklari[ders_harf] * ders_kredi)

    toplam = 0
    for a in krediler:
        toplam = toplam + a

print("eklediğiniz dersler")
print(ders_adlari)

kredileri_topla = 0
for b in krediler_toplami:
    kredileri_topla = kredileri_topla + b

krediler_toplami_for = 0
for c  in krediler:
    krediler_toplami_for = krediler_toplami_for + c

ortalama = kredileri_topla / krediler_toplami_for

print("ortalama : ", ortalama)

if ortalama < 1:
    print("KALDINIZ!")
else:
    print("BIR SONRAKİ DÖNEMDE BAŞARILAR :)")
