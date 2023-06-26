"""
class SuperKahraman():
    def __init__(self, isimInput, yasInput, meslekInput): # baslatma fonksiyonu
        self.isim = isimInput
        self.yas = yasInput
        self.meslek = meslekInput
    def ornekMethod(self):
        return f"Ben bir super kahramaným ve meslegim {self.meslek} "
        #print(f"Ben bir super kahramanim ve meslegim {self.meslek}")        

batman = SuperKahraman("Batman", 31, "Milyarder")    
print(batman.yas)    
batman.isim = "Bruce Wayne"
print(batman.isim) 
print(batman.ornekMethod()) 
"""

"""        
class Kopek ():
    yascarpani = 7
    def __init__(self,yas=5): # yas girilmez ise default 5 atanir
        self.yas = yas

    def insanyas (self):
        return Kopek.yascarpani * self.yas  # self.yascarpani de olur
        
benimKopek = Kopek(11)
print(benimKopek.yas)
print(benimKopek.insanyas())
print("Insanlarin yasi = " + str(benimKopek.insanyas()))   
  """  


# Inheritance -----------  miras almak / kalitim
"""
class Hayvan():
    def __init__(self, isim, yas, size):
        self.isim = isim
        self.yas = yas
        self.size = size
    def method1(self):
        return f"Hayvan sinif metot1"
    def method2(self):
        return f"Hayvan sinif metot2"    
    def method3(self):
        return f"Hayvan sinif metot3"         

class Kedi(Hayvan):
        
    def miyavla (self):
        print("miyav")        

kedim = Kedi("kedi", 23, "Caleb Martin")
print(kedim.method2())  
print(kedim.isim)  
print(kedim.size)   
"""

#Ozel methodlar (internetten bakarak isine yariyan metodu bulabilirsin -- special methods
"""
class Meyve():
    def __init__(self,isim,kalori):
        self.isim = isim
        self.kalori = kalori
    def __str__ (self):
        return f" {self.isim} Bu kadar kaloriye sahiptir =  {self.kalori}"
    def __len__(self):
        return self.kalori

meyvem = Meyve("muz", 150)
print(meyvem)
print(len(meyvem))     
"""
# hatalari ele almak /  try, except, else, finally
"""
def toplama(n1,n2):
    return n1+n2
#x = int(input("ilk numarayi giriniz: "))
#y = int(input("ikinci numarayi giriniz: "))       

while True: # programýn surekli calismasi icin
    try:
        b = int(input("numarani  giriniz: "))
    except:
        print("lutfen dogru numara giriniz")
        continue # dongunun basina donduruyor
    else:
        print(b)
       
    finally: # her turlu geliyor
        print("finally calisti") 

"""
        
        
        





