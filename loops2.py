# Çift sayıları yazdıran döngü

forRangeMin = int(input("Döngünün alt limitini belirleyiniz: "))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz: "))

for i in range(forRangeMin, forRangeMax+1):
    if i % 2 == 0 :
        print(i)

# Bu Python kodu, kullanıcıdan bir alt ve üst sınır belirlemesini isteyen bir döngü kullanarak, belirli bir aralıktaki çift sayıları ekrana yazdırmayı amaçlar.

#Kullanıcıya input() işlevi ile iki ayrı soru sorulur: Birincisi "Döngünün alt limitini belirleyiniz:" ve ikincisi "Döngünün üst limitini belirleyiniz:". Kullanıcı bu sorulara tamsayı değerleri girer.

#Girilen alt ve üst sınırlar forRangeMin ve forRangeMax adlı değişkenlere atanır.

#Ardından, for döngüsü range(forRangeMin, forRangeMax) ifadesi ile belirtilen aralıkta döner. Bu aralık, forRangeMin değerinden başlayarak forRangeMax değerine kadar olan ardışık tamsayıları içerir, ancak forRangeMax bu aralığın dışında kalır.

#Döngü içinde, her tamsayı (i) için bir kontrol yapılır. Eğer i çift bir sayıysa (yani i % 2 == 0 koşulu sağlanıyorsa), o zaman bu çift sayı ekrana yazdırılır.