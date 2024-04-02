import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

dosya_yolu = 'C:/Users/Lenovo/Desktop/Kurs/BTK_Veri Bilimi İçin Python ve Tensorflow/TenserFlow/bisiklet.xlsx'

dataFrame = pd.read_excel(dosya_yolu)
print(dataFrame.head(5))  # ilk 5 satir
print("")

#sbn.pairplot(dataFrame)
#plt.show()


# ------------------ Veriyi test/train olarak ikiye ayirmak ----------------------


from sklearn.model_selection import train_test_split # (sklearn.model_selection) modulu, 
# makine ogrenimi modellerinin egitimi, dogrulama ve model secimi icin cesitli islevler ve sınıflar saglar.
# train_test_split: Veri setini egitim ve test kumelerine bolme islemini gerceklestirir.

# y = wx + b  denklemini aklina getir
# y -> label   y'nin gitmek istediği nokta label
# x -> feature
 
y = dataFrame["Fiyat"].values # numpy array olarak tutar
#print(y)
print(type(y))
print(type(y[0]))
print("")

x = dataFrame[["BisikletOzellik1", "BisikletOzellik2"]].values
print(x)
print(type(x))
print(type(x[0]))
print(type(x[0][1]))
print("")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.33, random_state= 15)
print(len(x))
print(len(x_test))
print(x_train.shape)
print(x_test.shape)
print("")
print(len(y))
print(y_train.shape)
print(y_test.shape)
print(len(y_train))



# ---------------------------- Scaling ------------------------------------------------
# noronlara verilen veri setini kucultmek icin yapilir. Daha hizli olsun diye



from sklearn.preprocessing import MinMaxScaler # sklearn.preprocessing Veri on islemesi icin,
# Scikit-learn (sklearn) kütüphanesinin bir alt modülüdür.

scaler = MinMaxScaler() # MinMaxScaler veri olceklendirmesi yapmak için kullanilan bir class tir.
# veri setindeki degerleri belirli bir minimum ve maksimum araliga yeniden olceklendirir.
scaler.fit(x_train)
# fit yontemi, MinMaxScaler'i egitmek icin kullanilir. 
# Bu yontem, veri setindeki minimum ve maksimum degerleri ogrenir.
x_train = scaler.transform(x_train) # x_train deki degerler 0 ile 1 arasindaki degerler ile yeniden olceklendirildi / veri kuculmus oldu
x_test = scaler.transform(x_test) # x_test deki degerler 0 ile 1 arasindaki degerler ile yeniden olceklendirildi




# -------------------------- Modeli olusturma --------------------------------------

import tensorflow as tf
from tensorflow.keras.models import Sequential # Sequential bizim modelimizin sinifi,
# icersinde hangi katmanlarla calisicaz onu belirtiyoruz, Kisacasi modeli olusturuyoruz
from tensorflow.keras.layers import Dense  # model icersinde katmanlari koyuyoruz, katmanlarla calismak

model = Sequential() # baslangicta boş bir Sequential modeli olusturulur. 
# Ardindan, model.add() yontemi kullanilarak ardisik olarak katmanlar eklenir.
model.add(Dense(4, activation="relu")) # ile ilk katman (gizli katman) eklenir.
model.add(Dense(4, activation="relu")) # 4 tane noron olacak, act fonksiyon= relu
model.add(Dense(4, activation="relu"))
# 3 tane hidden layer oldu

model.add(Dense(1)) # Son olarak cikti katmani eklemeliyiz, 1 tane cikti yeterli olucaktir

model.compile(optimizer= "rmsprop", loss= "mse") # (optimizer=) Modelin optimize edici (optimizer) 
#  algoritmasini belirtir. (rmsprop) degeri, Root Mean Square Propagation algoritmasini temsil etmektedir.
# (loss=) kayıp fonksiyonunu belirtir.   mse= "Ortalama Kare Hatası" 

#"loss" (kayıp), bir makine öğrenimi modelinin performansını ölçen bir metriktir. 
# Modelin tahmin ettiği değerlerle gerçek değerler 
# arasındaki farkı temsil eder. Kayıp değeri ne kadar düşükse, 
# modelin tahminleri gerçek değerlere o kadar yakın demektir.


# Modelimiz Hazir


# -------------------- Modeli egitme kismi (Training) --------------------------

model.fit(x_train, y_train, epochs= 250) # x_train'i y_train ile egiticez
# epochs=1 olması tum veri setini 1 kez gecmesi demek

model.history.history  # model.history.history, bir Keras modelinin egitim 
# islemi sirasinda kaydedilen egitim gecmisiyle iliskili bir sozlugu 
# temsil eder. Bu sozluk, egitim surecinde takip edilen metriklerin 
#(kayıp, dogruluk, vb.) degerlerini icerir.

# type(model.history.history) ->   dict


loss = model.history.history["loss"] 
# model.history.history['loss'] ifadesi egitim surecindeki her epoch
# icin kaydedilen kayıp degerlerini iceren bir dizi veya liste dondurecektir.
# len(loss) = epoch sayısı

sbn.lineplot(x= range(len(loss)), y= loss)
plt.show()
# loss icersinde kac tane veri varsa onu gostersin -> range(len(loss))

trainLoss = model.evaluate(x_train, y_train, verbose=0)
testLoss = model.evaluate(x_test, y_test, verbose=0)
print("")
print("TrainLoss = ",trainLoss)
print("") # birbirine yakin mi değil mi bak
print("TestLoss = ",testLoss )



# -------------------- Model degerlenidirilmesi / Tahmin ------------------------------

testTahminleri = model.predict(x_test) # x_test degerlerini verince gercekte sonuclar ne olacak
# biliyoruz (y_test olucak), modele x_test'i vererek bir tahmin yapılır ve y_test ile 
# kiyaslanir, yani bu sonuc (y_test_train gibi ) bir sey bulmus olcaz

# x_test.shape = (330,2) oldugu icin pd.Series olması icin 1 dimension olmalı
# reshape edilmeli
testTahminleri_Series = pd.Series(testTahminleri.reshape(330,))

gercek_y = pd.DataFrame(y_test, columns= ["Gercek y"])

tahminDF = pd.concat([gercek_y, testTahminleri_Series], axis=1)
tahminDF.columns = ["Gercek y", "Tahmin y"]  

sbn.scatterplot(x= "Gercek y", y= "Tahmin y", data = tahminDF)
plt.show()



# ----- Hatalarin Gercek degerini (absolute) degerini alma, Gercek Hata ne kadar cikiyor onu -----
# -- gorebiliriz. Sapma icin bir mantik verebilir

from sklearn.metrics import mean_absolute_error, mean_squared_error

mean_absolute_error(tahminDF["Gercek y"], tahminDF["Tahmin y"])
# sonuc (7.2) cikiyor. (7.2)'lik hata var demek 
mean_squared_error(tahminDF["Gercek y"], tahminDF["Tahmin y"])
# (80.8)
# dataFrame.describe(), yaz karsilastir

# yeni 1 tane bisiklet geldi diyelim
yeniBisiklet = [[1749.4, 1748.8]] # type = list
yeniBisikletOzellikleri = scaler.transform(yeniBisiklet)
#array([[0.41445056, 0.39349564]])
model.predict(yeniBisikletOzellikleri) #array([[743.9471]], dtype=float32)
                

# -------------------- Modeli kaydetme ---------------------------------
from tensorflow.keras.models import load_model

model.save("bisiklet_modeli.h5") # bunuz uzantisi h5
# sonradan cagırmak icin
sonradanCagirModel = load_model("bisiklet_modeli.h5")
# Yeni veri üzerinde tahmin yapma
sonradanCagirModel.predict(yeniBisikletOzellikleri)

