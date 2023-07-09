import numpy as np
import pandas as pd
"""
a = pd.Series([10,20,30])
print(a)
print("")

b = pd.Series(["mess", "sadf", "etew"], [1, 2, 3])
print(b)
print("")

benimSozluk = {"Ati": 20, "Zey": 16, "Motiv": 131}
r = pd.Series(benimSozluk)
print(r)
print("")

aa = np.arange(0,6,2)
bb = pd.Series(aa)
print(bb)
print("")

yaslar = [38, 36, 31]
isimler = ["LeBron", "Messi", "Harry"]
c = pd.Series(data= yaslar, index=isimler)
d = pd.Series(isimler,yaslar)
print(c)
print("")
print(d)
print(d[31])    
"""
"""
yarismaSonucu1 = pd.Series([31, 62, 99], ["Osayi", "CR7", "Dünyadan Atlas'a"]) # sagdakiler index, soldakiler data
yarismaSonucu2 = pd.Series([66, 77, 88, 98], ["Dünyadan Atlas'a", "CR7", "Osayi", "Mo"])
print(yarismaSonucu1["CR7"])
print("")
sonSonuc = yarismaSonucu1 + yarismaSonucu2
print(sonSonuc)   
"""

# ------------------------ DataFrame ------------------------
"""
data = np.random.randint(1,300, (4,3))
print(data)
print(type(data))
print("")

dataFrame = pd.DataFrame(data)
print(dataFrame)
print("")
#print(dataFrame[1][0]) # coloumn ile row ters 

yenidataFrame = pd.DataFrame(data, columns= ["Maas", "Yas", "Saat"], index=["LBJ", "Salah", "Valencia", "Tevez"])
print(yenidataFrame)
print("")
print(yenidataFrame["Yas"])
print("")
print(yenidataFrame.loc["Salah"])
print("")
print(yenidataFrame.iloc[1]) # index loc
"""

"""
data = np.random.randn(4,3)

dataFrame = pd.DataFrame(data)

yenidataFrame = pd.DataFrame(data, columns= ["Maas", "Yas", "Saat"], index=["LBJ", "Salah", "Valencia", "Tevez"])
print(yenidataFrame)
print("")

yenidataFrame["Emeklilik"] = yenidataFrame["Yas"] *2
print(yenidataFrame)
print("")

print(yenidataFrame.drop("Saat", axis = 1)) 
# axis=1, sutun bazında işlem yapılacagını belirtir.
# axis=0, satır bazında işlem yapılacagını belirtir.
print("-----------------------------------------------------------------")

sıfırdanBuyuk = yenidataFrame > 0
print(sıfırdanBuyuk)
print("")
#print(yenidataFrame[sıfırdanBuyuk])
print("")
#print(yenidataFrame[yenidataFrame["Yas"] > 0]) # Yas'ı 0'dan kucuk olanlar silindi.
print("")
#print(yenidataFrame[yenidataFrame["Saat"] > 0])
print("")

indexlistesi = ["James", "Mo", "Enner", "Carlos"]
yenidataFrame["Yeni Index"] = indexlistesi
print(yenidataFrame)
print("")

yenidataFrame.set_index("Yeni Index")
print(yenidataFrame) # print(yenidataFrame.set_index("Yeni Index")) yazılırsa olur
print("")

yenidataFrame.set_index("Yeni Index", inplace= True)
# yenidataFrame.index.names = ["Cukkala"]
print(yenidataFrame)
print("") 
"""

# ----------------- Multi Index -----------------------
"""
ilkIndexler = ["Simpson", "Simpson", "Simpson", "South Park","South Park","South Park"]
icIndexler = ["Homer", "Bart", "Marge", "Carmen", "Kenny", "Kyle"]
birlesmisIndex = list(zip(ilkIndexler, icIndexler))
print(birlesmisIndex)
print("")

birlesmisIndex = pd.MultiIndex.from_tuples(birlesmisIndex)
print(birlesmisIndex)
print("")

CizgiFilmListe = [[40,"A"], [10,"B"], [30,"C"], [9,"D"], [10,"E"], [11,"F"]]
CizgiFilmNumpyDizi = np.array(CizgiFilmListe)

CizgiFilmDataFrame = pd.DataFrame(CizgiFilmNumpyDizi, index= birlesmisIndex, columns= ["Yas", "Meslek"]) #CizgiFilmListe ' de olur aslinda
print(CizgiFilmDataFrame)
print("")
print(CizgiFilmDataFrame.loc["Simpson"].loc["Bart"])
print("")

CizgiFilmDataFrame.index.names = ["Film Adı", "Name"]
print(CizgiFilmDataFrame)  
"""

#   ------------ Hava durumu ----------------------
"""
sozluk = {"Istanbul" : [39, 29, np.nan], "Ankara": [20, np.nan, 25], "Izmir" : [40,39,38], "Antalya": [45, np.nan, np.nan]}
havaDataFrame = pd.DataFrame(sozluk, index= ["Pztesi", "Sali", "Carsamba"])
print(havaDataFrame)
print("")
print(havaDataFrame.dropna()) # axis = 0
print("")
print(havaDataFrame.dropna(axis=1))
print("")
print(havaDataFrame.dropna(axis=1, thresh=2)) # tresh (tres hold) kaca kadar limit koy manasina geliyor
print("")
havaDataFrame.fillna(20, inplace=True)
print(havaDataFrame)
"""

# ---------------------------- Groupby -----------------------------------------------
"""
massSozluk = {"Departman" : ["Yazilim", "Yazilim", "Finans", "Finans", "Hukuk", "Hukuk"],
              "Calisan Ismi": ["Harden", "CP3", "Chef", "Klay", "Draymond", "Iggy"],
              "Maas" : [400, 300, 600, 400, 298.5, 101] }
maasDataFrame = pd.DataFrame(massSozluk)
print(maasDataFrame)
print("")

grupObjesi = maasDataFrame.groupby("Departman") # Departman kolonuna gore gruplandırma yapiyor
print(grupObjesi.count())
print("")
gruplama_sonuclari = grupObjesi.count()
print(gruplama_sonuclari)

gruplama_sonuclari = grupObjesi.describe()
print(gruplama_sonuclari)  
"""

# ---------------- Concat (birlestirme) --------------
"""
sozluk1 = {"Isım": ["Dennis", "Dlo", "AD", "Hilly"],
           "Spor": ["Kosu", "Yüzme", "Kosu", "Basketbol"],
           "Kalori":[100, 200, 300, 400] }
dataFrame1 = pd.DataFrame(sozluk1, index= [0, 1, 2, 3])

sozluk2 = {"Kalori":[200, 100, 50, 300],
           "Spor": ["Futbol", "Soccer", "Tır", "Hokey"],
            "Isım": ["Malik", "Gabriel", "Tristan", "Rui"]}
dataFrame2 = pd.DataFrame(sozluk2, index= [4, 5, 6, 7])

sozluk3 = {"Isım": ["Kuzma", "Caruso", "Gasol", "Troy"],
           "Kalori":[300, 400, 500, 250],
           "Spor": ["F1", "Jump", "Golf", "Basketbol"] }
dataFrame3 = pd.DataFrame(sozluk3)

sondataFrame = pd.concat([dataFrame1, dataFrame2, dataFrame3], axis=0)
print(sondataFrame) # Concat icine (ignore_index =True) yaz index prob kurtul
print("")

# ---------- Merge (birlestirme,kaynastirma) ------------

sozluk1 = {"Isim": ["Dennis", "Dlo", "AD", "Hilly"],
           "Spor": ["Kosu", "Yüzme", "Kosu", "Basketbol"] }
dataFrame1 = pd.DataFrame(sozluk1, index= [0, 1, 2, 3])


sozluk2 = {"Isim": ["Dennis", "Dlo", "AD", "Hilly"],
           "Kalori": [100, 63, 566.5, 465] }
dataFrame2 = pd.DataFrame(sozluk2, index= [5, 85, 2, 3])


mergedataFrame = pd.merge(dataFrame1, dataFrame2, on="Isım")
# on=  hangi kolon ustunden ortak islem yapıcaz
print(mergedataFrame)  
"""

# ---------------------- Pandas Operasyonlar --------------------------------------
"""
massSozluk = {"Departman" : ["Yazilim", "Yazilim", "Finans", "Pazarlama", "Yazilim", "Hukuk"],
              "Calisan Ismi": ["Harden", "CP3", "Chef", "Klay", "Draymond", "Iggy"],
              "Maas" : [400, 300, 600, 400, 298.5, 101] }
maasDataFrame = pd.DataFrame(massSozluk)
print(maasDataFrame)
print("")

print(maasDataFrame["Departman"])
print("")
print("-------------------------------------------")
print("")
print(maasDataFrame["Departman"].unique())
print("")
print("departman sayisi: ", maasDataFrame["Departman"].nunique())
print("")
print(maasDataFrame["Departman"].value_counts())
print("")
print("-------------------------------------------")
print("")
def netmaas(maas):
    return 0.6 * maas
a = maasDataFrame["Maas"].apply(netmaas)
print(a)
print("")
#inplace=True olarak yapmanın bir yolu yoktur. apply() yöntemi, orijinal DataFrame'i değiştirmek yerine bir kopya döndürür.

print(maasDataFrame.isnull()) # isnull() icersinde NAN değer var mı bakıyor
print("")
"""

# --------------------------- Pivot Table --------------------------
"""
sozluk = {"Departman" : ["Yazilim", "Yazilim", "Finans", "Finans", "Hukuk", "Hukuk"],
              "Calisan Ismi": ["Harden", "CP3", "Chef", "Klay", "Draymond", "Iggy"],
              "Maas" : [400, 300, 600, 400, 298.5, 101] }
karakterDF = pd.DataFrame(sozluk)
print(karakterDF)
print("")

sonDF = karakterDF.pivot_table(values=["Maas"], index=["Departman","Calisan Ismi"])
print(sonDF) 
"""
 
# --------------------------- Excel ----------------------------------
"""
data = pd.read_excel("pandas_alistirma.xlsx")
data = data.set_index("Unnamed: 0")
data.index.names = ["INDEX"]
print(data)
print(type(data))
print(type(data["Yas"]))
print(type(data["Yas"][2]))
print("")

doludegerler_data = data.dropna()
doludegerler_data.to_excel("yenimaas.xlsx") # yenimaas isimli bir excel dosyası olusturup icine yazar 

"""

