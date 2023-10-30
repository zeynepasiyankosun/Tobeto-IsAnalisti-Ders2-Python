#Diziye kullanıcıdan aldığımız sayıları ekleme

sayilar = []

for i in range(3):
    sayilar.append(int(input(f"{i+1}. sayıyı giriniz: ")))   #append() bir liste metodudur ve Python'da listelere yeni öğeler eklemek için kullanılır. 

    sayilar.sort()   #sort() işlevi, Python'da bir liste içindeki öğeleri sıralamak için kullanılır. 
    print(sayilar)

    #büyükten küçüüğe sıralamak için: sayilar.sort(reverse=True)  

    print(min(sayilar))
    print(max(sayilar))