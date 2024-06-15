                          # Dic
"""benimsozluk = {"karpuz" : 200, "elma" : 654, 'oyy' : 3131 }
benimsozluk ["elma"] = "yuz yetmiş asf"
print(f"Karpuzun kalorisi= {benimsozluk['karpuz']}") 
# print(f"safsafsa {}") print f komutu

sozluk = {1: "saf", -2: "op", 465: 'swd' }
print(sozluk[1]) 

yeniDictionary = {"anahtar1": 100, "anahtar2": [1, 2, 3, 4.52, 'atıl'], "anahtar3": {"anahtar9": 4, 5: "sadfwq"}}
print(yeniDictionary["anahtar3"]["anahtar9"])
print(yeniDictionary["anahtar2"][-1])
"""
 #                         if else
"""
benimsozluk = {"karpuz" : 200, "elma" : 654, 'oyy' : 3131 }       
a = benimsozluk.items()    
print(benimsozluk.items())
print(type(a))
print("")

if "karpuz" in benimsozluk: # benimsozluk.keys() yazarsak daha iyi olur
    print("str var")
else:
    print("str yok")    

if 200 in benimsozluk: # benimsozluk.values() yazarsak 200'ü bulur
    print(" var")
else:
    print("yok")   
"""
#                     Veri Bilim Fayadalı METOTLAR 
"""
for eleman in enumerate(list(range(5,10,2))):
    print (eleman)
    print(type(eleman)) 
print("")
for (index, numara) in enumerate(list(range(5,10,2))):
    print (index)
print("")        
for (index, numara) in enumerate(list(range(5,10,2))):
    print (numara)
"""

#                Zip
"""
yemeklistesi = ["muz", "karpuz", "elma"]
kalorilistesi = [100, 200, 300]
gunlistesi = ["pztesi", "salı", "cuma"]

x = zip(yemeklistesi, kalorilistesi, gunlistesi)
print (type(x))
print(x)
zip_x = list(zip(yemeklistesi, kalorilistesi, gunlistesi))
print (zip_x)
print("")
print(zip_x[0])

for eleman in zip_x:
    print(type(eleman)) 
    """
#               liste örnek
"""yenliste = [number for number in list(range(0,10))]
print(yenliste)
yenliste = [number * 5 -1 for number in list(range(0,10))]
print(yenliste) """

#             fonksiyonlar
"""
def Toplama(num1=20 ,num2=13):
    sum = num1 + num2
    print(sum, end=" ")
    print("yep")

print (Toplama())
print(Toplama(20,564))   
print("") 

def yenitoplama(num1=20 ,num2=13):
    return num1 + num2        

y = yenitoplama(496,26)
print(y)

def bolme(numara):
    return numara / 2
litt = list(range(0,11))
yeni = []
for eleman in litt:
    yeni.append(bolme(eleman))
print(yeni)  
"""  

#               args & kwargs
"""
def fonk(*args): # args ile istediğim kadar değer girebilirim
    return (args) # return kullanırsan tuple döndürür, yoksa NoneType olur
t =  fonk (652, 'safas', [541, 2, 63, {2, 32}])
print(t)       

def yeniToplama(*args): 
    return sum(args)  
sonuc = yeniToplama(20,6,66,16,46,-185)
print(sonuc)

def ornekFonk(**kwargs): # anahtar kelimeler ile
    return (kwargs) # return kullanırsan dic döndürür, yoksa NoneType olur
s = ornekFonk(karpuz = 200, elma = 654, oyy = 3131)
print(s) 
"""
"""
#                    map
def bolme(numara):
    return numara / 2
litt = list(range(0,11))

yeni = list(map(bolme, litt))
print(yeni) 

liste = ["ara", "grgrg", "awra", "fasf", "reg"]
def ara (string):
    return "a" in string
sonuncListe = list(map(ara, liste))
print(sonuncListe)
print("")

#                 filter
sonuncListe = list(filter(ara, liste))
print(sonuncListe)
print("")

#               lambda
carpma = lambda numara : numara * 3
print(carpma(10)) 

ornekliste = [10, 20, 56]
ss = list(map(lambda numara : numara * 4, ornekliste))  
print(ss) 
"""









               