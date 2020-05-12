#string to int

x = input("1.sayı: ")
y = input("2 sayı: ")

print(type(x)) 
print(type(y)) 

toplam = x + y
print(toplam)                     # ekrana yazdirirken string ifade olarak algiladigindan dolayı sayilari toplamadi yanyana yazdi bu yuzden sonuc yanlis oldu. bu durumu duzeltmek için string'ten int' veri tipine donusturmemiz gerek

print("doğrusu şöyle olmalı") 

toplam = int(x) + int(y)
print(toplam)

print("---------------")

a = 10
b = 4.1
isim = "hatice"
ogrenciMi = True

print(type(a))
print(type(b))
print(type(isim))
print(type(ogrenciMi))

print("---------------")

#int to float

a = float(a)                      # int olan a degiskeni floata donusturduk
print(a)
print(type(a))                    # donusup donusmedigini kontrol edelim

print("---------------")

#float to int

a = int(b)                        # float olan a degiskeni inte donusturduk
print(b)
print(type(b))

print("---------------")

# bool to string

ogrenciMi = str(ogrenciMi)        # bool olan a degiskeni stringe donusturduk
print(ogrenciMi)
print(type(ogrenciMi))

print("---------------")

#bool to int

ogrenciMi = int(ogrenciMi)        # bool olan a degiskeni inte donusturduk
print(ogrenciMi)
print(type(ogrenciMi))