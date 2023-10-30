#Dizi elemanlarını listeleme

ogrenciler = ["Şeyma", "Zeynep", "Emre", "Can"]

print(len(ogrenciler))  #len() işlevi, Python'da kullanılan veri yapısının (örneğin, bir liste, dize, demet vb.) uzunluğunu, yani içindeki öğe sayısını döndüren bir işlevidir. 

for i in range(len(ogrenciler)):
    print(ogrenciler[i])

#Bu kod, ogrenciler listesindeki öğeleri indekslerini kullanarak sırayla ekrana yazdırır.

#şu şekilde de yazılabilir:

for i in range(len(ogrenciler)):
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")
