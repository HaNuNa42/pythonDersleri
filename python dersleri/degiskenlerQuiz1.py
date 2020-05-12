""" 
    1- bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    müşteri adı
    müşteri soyadı
    müşteri adı + soyadı
    müşteri cinsiyet
    müşteri tc kimlik
    müşteri doğum yılı
    müşteri adres bilgisi
    müşteri yaşı
"""

musteriAdi = "hatice"
musteriSoyadi = "nur"
musteriAdSoyad = musteriAdi + " " + musteriSoyadi
musteriCinsiyet = "kadın"
musteriTcKimlik = "12345678912"
musteriDogumYili = 1900
musteriAdres = "karatay konya"
musteriYasi = 2020 - musteriDogumYili


"""
    2- aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

    sipariş 1 => 100 TL
    sipariş 2 => 168.5 TL
    sipariş 3 => 6874.63 TL

"""
siparis1 = 100
siparis2 = 168.5
siparis3 = 6874.63
toplam = siparis1 + siparis2 + siparis3
print ("Toplam: ", toplam)