#continue ifadesi, Python'da döngüler içinde kullanılan bir kontrol ifadesidir.
#Bir döngü içinde continue ifadesi bulunduğunda, bu ifade döngü içindeki o anki döngü adımını atlar ve bir sonraki döngü adımına geçer.
#Yani, döngüyü sonlandırmaz, sadece o anki adımı atlayarak bir sonraki adıma geçer.

ogrenciler = ["Şeyma", "Zeynep", "Emre", "Can"]

for i in ogrenciler:
    if i== "Şeyma":
        continue 
    print(f"Öğrenci: {i}")

    