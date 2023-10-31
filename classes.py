#Python'da sınıflar, nesne yönelimli programlamanın temel bir bileşenidir.
#Sınıflar, benzer özelliklere ve davranışlara sahip nesneleri gruplamak ve bu nesneleri oluşturmak için kullanılırlar.

class Human:
    #property, attribute (özellik, nitelik)
    name= "Aşiyan"
    age= 29

#Python'da "property" ve "attribute" terimleri, nesne yönelimli programlamada kullanılan önemli kavramlardır.
#Her ikisi de bir nesnenin özelliklerini tanımlamak için kullanılır, ancak farklı işlevlere sahiptirler.


#methods, davranışlar / Python'da bir sınıf içinde tanımlanan "methods" (metodlar), nesnelerin davranışlarını veya işlevlerini tanımlayan işlevlerdir.
#Bir nesnenin ne tür işlemleri yapabileceğini ve nasıl tepki verebileceğini belirlerler.

def talk(message):
    print(message)

def walk():
    print("Walking")