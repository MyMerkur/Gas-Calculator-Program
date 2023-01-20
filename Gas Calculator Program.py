print("Şehir İçi")
km100_başına_şehiriçi_yakıt_benzinli = print(
    "100 km'de \n1.2 motor --> 6 \n1.4 motor --> 6.8 \n1.6 motor --> 6 \n2.0 motor --> 10.1")
print("Şehir Dışı")
km100_başına_şehirdışı_yakıt_benzinli = print(
    "1.2 motor --> 4.3 \n1.4 motor --> 4.9 \n1.6 motor --> 5.1 \n2.0 motor --> 7.2")
# Güncel benzin fiyatını (19.50) / (max/v 100km/h) sabit olarak alıyorum.

araç = input("Aracınızın Hangi Yakıt Tipini Kullandığını Giriniz : "), "Benzin=1  Dizel=2"
yol = int(input("Aracınız İle Gideceğiniz Mesafe Kaç Km:"))
iç_dış = str(input("Gideceğiniz Yer Şehir İçi / mi Şehir Dışımı (İç=1 , Dış=2):")), "İç=1  Dış=2"
motor = input("Aracınızın Motor Hacmi Nedir:")

benzinfiyatı = (19.50)
hesaplamaiç1_2 = benzinfiyatı * yol * 6
hesaplamaiç1_4 = benzinfiyatı * yol * 6.8
hesaplamaiç1_6 = benzinfiyatı * yol * 6
hesaplamaiç2_0 = benzinfiyatı * yol * 10.1

hesaplamadış1_2 = benzinfiyatı * yol * 4.3
hesaplamadış1_4 = benzinfiyatı * yol * 4.9
hesaplamadış1_6 = benzinfiyatı * yol * 5.1
hesaplamadış2_0 = benzinfiyatı * yol * 7.2

# tutariç = benzinfiyatı*yol*km100_başına_şehiriçi_yakıt_benzinli
# tutardış = benzinfiyatı * yol * km100_başına_şehirdışı_yakıt_benzinli

if araç == '1' and iç_dış == '1':
    print("Benzinli aracınızın Şehir içi Yakıt tüketimi aşşağıdaki gibidir.")
else:
    ("Girdiğiniz Değerlerin Doğru Olup Olmadığından Emin Olunuz")
if motor == '1.2':
    print("Toplam tutar {}'dır.".format(hesaplamaiç1_2))
elif motor == '1.4':
    print("Toplam tutar {}'dır.".format(hesaplamaiç1_4))
elif motor == '1.6':
    print("Toplam tutar {}'dır.".format(hesaplamaiç1_6))
elif motor == '2.0':
    print("Toplam tutar {}'dır.".format(hesaplamaiç2_0))

if araç == '1' and iç_dış == '2':
    print("Benzinli aracınızın Şehir dışı Yakıt tüketimi aşşağıdaki gibidir. ")
else:
    ("Girdiğiniz Değerlerin Doğru Olup Olmadığından Emin Olunuz")
if motor == '1.2':
    print("Toplam tutar {}'dır.".format(hesaplamadış1_2))
elif motor == '1.4':
    print("Toplam tutar {}'dır.".format(hesaplamadış1_4))
elif motor == '1.6':
    print("Toplam tutar {}'dır.".format(hesaplamadış1_6))
elif motor == '2.0':
    print("Toplam tutar {}'dır.".format(hesaplamadış2_0))











