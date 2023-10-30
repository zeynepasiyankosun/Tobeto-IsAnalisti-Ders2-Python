#FOR DÖNGÜSÜ

for i in range():  #Python'da for döngüsünün range() işlevi ile kullanıldığında for i in range() ifadesi belirli bir aralıktaki değerleri işlemek için kullanılır. range() işlevi, başlangıç, bitiş ve adım parametreleri alabilir ve ardışık sayılar oluşturur. 
    print(i)

#Python'daki range() işlevi veya for döngüsünde kullanılan start, stop ve step ifadeleri şunları ifade eder:
#start: Bu, ardışık sayıların başlangıç değerini temsil eder. Yani ardışık sayılar bu değerden başlar. Varsayılan olarak, start değeri 0'dır, yani başlangıç değeri 0'dır.
#stop: Bu, ardışık sayıların sona ereceği (bitiş) değeri temsil eder. Ancak bu değer, ardışık sayılarla kendisi dahil edilmez. Yani, ardışık sayılar stop değerine eşit veya daha küçük değerlere kadar gider.
#step: Bu, ardışık sayılar arasındaki adım veya artış miktarını temsil eder. Varsayılan olarak step değeri 1'dir, yani ardışık sayılar birer birer artar. Ancak isteğe bağlı olarak farklı bir adım miktarı belirtilebilir, bu sayede ardışık sayılar özelleştirilebilir.

biggestValue = 0

for i in range(5):
    sayi = int(input(f"{i+1}. Sayıyı Giriniz: ")) #Python'daki f-string (format string) özelliği, metin dizilerini biçimlendirmek ve değişken değerlerini metin içine yerleştirmek için kullanılan bir araçtır. F-stringler, metin içinde süslü parantezlerle çevrili değişkenlerin veya ifadelerin doğrudan metin içine yerleştirilmesini sağlar. Bu, metni okunaklı ve daha esnek hale getirir.
    if sayi > biggestValue:
        biggestValue = sayi 

#Yukarıdaki kod kümesi, kullanıcının 5 adet sayı girmesini isteyen bir döngüyü ve bu girdiler arasında en büyük sayıyı bulmayı amaçlar. 
# biggestValue adlı bir değişken başlangıçta 0 değeriyle başlatılır. Bu değişken, kullanıcının girdiği sayılar arasında en büyük değeri saklayacaktır.
# for döngüsü, 0'dan 4'e kadar olan sayıları temsil eden i değişkeni üzerinden 5 kez döner. Kullanıcı her döngü adımında bir sayı girmelidir.
# Kullanıcıdan sayı girişi istenir ve bu sayı sayi adlı bir değişkene atanır. input() işlevi kullanıcıdan girdi alır ve int() işlevi ile bu girdi bir tamsayıya dönüştürülür.
# Ardından, girilen sayi değeri, şu koşulla karşılaştırılır: sayi değişkeni, biggestValue değişkeninden daha büyükse, biggestValue değişkeni güncellenir. Böylece döngü her döndüğünde, en büyük girilen sayıyı takip eder.
# Döngü tamamlandığında, kullanıcının girdiği 5 sayı arasındaki en büyük sayıyı biggestValue değişkeninde saklayacaksınız.

print(f"Girdğiniz Sayılar Arasında En Büyük Olan Say: {biggestValue}")




