#def (definition), Python'da bir fonksiyon (function) tanımlamak için kullanılan bir anahtar kelimedir.
#Python'da fonksiyonlar, belirli bir işlevi veya görevi gerçekleştiren kod bloklarıdır ve bu kodu daha sonra kullanmak için bir ad (isim) ile tanımlarız.

def ortalamaHesapla() : #ifadesindeki parantezler, bir Python fonksiyonunun tanımında kullanılan parametre listesini belirtir. Fonksiyonun adı ortalamaHesapla ve bu fonksiyon herhangi bir parametre almadığı için parantez içi boştur.
    final =75
    vize =48
    ortalama = (vize*0.4) + (final*0.6)
    print(ortalama)

def ortalamaHesaplaVeDöndür():
    final =75
    vize =48
    ortalama = (vize*0.4) + (final*0.6)
    return ortalama #ifadesi, hesaplanan ortalama değerini geri döndürür. Yani, fonksiyon çağrıldığında, bu ortalama değeri kullanıcıya veya başka bir amaçla kullanılmak üzere döner.



ortalamaHesapla()
print(ortalamaHesaplaVeDöndür())

def ortalamaHesaplaVeYazdir(vize,final):
    return (vize*0.4) + (final+0.6)

print (ortalamaHesaplaVeYazdir(66,77))