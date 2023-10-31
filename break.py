#break 

#break ifadesi, Python'da döngülerin (örneğin for ve while döngüleri) çalışmasını anında sona erdirmek için kullanılır.
#Bir break ifadesi bulunduğu yerdeki döngüyü derhal terk eder ve döngü sonlanır.
#break ifadesi, genellikle belirli bir koşul karşılandığında döngüyü sonlandırmak için kullanılır.

ogrenciler = ["Şeyma", "Zeynep", "Emre", "Can"]
for i in range(len(ogrenciler)):
    if i >3 :
        break 
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")

