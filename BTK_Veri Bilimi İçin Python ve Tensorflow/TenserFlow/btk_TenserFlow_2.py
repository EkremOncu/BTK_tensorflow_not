import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sbn

DataFrame = pd.read_excel("merc.xlsx")
# dataFrame.head()
DataFrame.isnull().sum() # veri setinde null(NaN) degerler var mi ? 
"""year            0
   price           0
   transmission    0
   mileage         0
   tax             0
   mpg             0
   engineSize      0
   dtype: int64        """

sbn.distplot(DataFrame["price"])
plt.show()

sbn.countplot(DataFrame["year"]) #2020 model 719 tane var
plt.show()

DataFrame.corr() # verilerin birbirleri arasindaki korelasyonu
# Pozitif bir korelasyon 1'e yaklaşırken, negatif bir korelasyon 
# -1'e yaklaşır. Sıfıra yakın bir korelasyon ise 
# iki değişken arasında bir ilişkinin olmadığını gösterir.
DataFrame.corr()["price"].sort_values() # siraliyor

sbn.scatterplot(x = "mileage", y = 'price', data= DataFrame)
plt.show()

DataFrame.sort_values("price", ascending= False).head(20)

# sbn.displot grafigine bakarak en yuksek price li arabaları 
# cıkarıcaz, daha iyi bir veri elde etmek icin

""" bi verinin %99'unu alirsak yani %1'ini cikarirsak
onemli bir sorun olmaz ->  len(dataFrame) * 0.01 = 131  """

yeniDataFrame = DataFrame.sort_values("price", ascending= False).iloc[131:]

sbn.distplot(yeniDataFrame["price"])
plt.show()

yeniDataFrame.groupby("year").mean()["price"]
"""
year
1970    24999.000000
1997     9995.000000
1998     8605.000000
1999     5995.000000
2000     5743.333333
2001     4957.900000
2002     5820.444444
2003     4878.000000
2004     4727.615385
2005     4426.111111
2006     4036.875000
2007     5136.045455
2008     6967.437500
2009     6166.764706
2010     8308.473684
2011     8913.459459
2012    10845.140351
2013    11939.842466
2014    14042.936864
2015    16647.822222
2016    19223.558943
2017    21356.280421
2018    24800.844506
2019    30289.524832
2020    34234.794872
Name: price, dtype: float64

kac tane 1970 model araba var ?

yeniDataFrame.loc[yeniDataFrame['year'] == 1970]

#      year  price  transmission  mileage  tax   mpg   engineSize
12072  1970  24999    Automatic    14000   305   39.2    0.0 

1 satir gosteriyor, yani 1 tane varmis

yukarıya bakacak olusak 1970 model bir araba cok yüksek bir fiyata 
satilmis (muhtemelen istisna, klasik antika gibi bir araba olabilir)
bunu atip veriyi incelemek daha doğru bir sonuc verir
"""

yeniDataFrame[yeniDataFrame['year'] != 1970].groupby("year").mean()["price"]
# 1970'liler haric donduruyor

yeniDataFrameEksi1970 = yeniDataFrame[yeniDataFrame['year'] != 1970]

# transmission kolunundan kurtulmamiz lazim cunku numeric deger yok
dataFrame = yeniDataFrameEksi1970.drop("transmission", axis=1)

y = dataFrame["price"].values # numpy dizisine cevrildi
x = dataFrame.drop("price", axis=1).values # x.shape = (12987, 5)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=10)

len(x_train) # 9090
len(x_test)  # 3897
len(y_train) # 9090
len(y_test)  # 3897

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# x.shape = (12987, 5) 5 tane ozelligimiz var bu sebeple en az 5 katman olmali,

model = Sequential()
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(1))

model.compile(optimizer= "adam", loss="mse")

model.fit(x=x_train,y= y_train, validation_data=(x_test,y_test), batch_size=250,epochs=300)
# validation_data= (dogrulama datası)-> (x_test,y_test)daha once manuel olarak
# yaptıgım (x_test)'i (y_test) ile kiyaslama islemini cok kolay hale getiriyor 
## Elimizde cok data oldugunda bir anda modele vermek modeli yorar
## batch'ler halinde vermeliyiz 

kayipVerisi = pd.DataFrame(model.history.history)
kayipVerisi.head(10)
"""
         loss     val_loss
0  672142400.0  688096064.0
1  672113280.0  688052480.0
2  672040896.0  687930432.0
3  671832256.0  687579264.0
4  671271104.0  686703424.0
5  669940864.0  684657408.0
6  666827520.0  679941504.0
7  660122560.0  670414912.0
8  647252992.0  652935360.0
9  624797952.0  623691072.0
"""
kayipVerisi.plot() 
""" 
Gayet guzel bir grafik, sebebi: 
. yukarıdan asagiya doğru iniyor
. sifira yaklasiyor
. loss(kayip) ve val_loss(dogrulama kaybi) birlikte hareket ediyor. Ozellikle sonlara dogru

# Mesela epochs'u fazla verirsek overfitting durumu olusabilir, yani noronlar
problemi cozmek yerine su an elimizde bulunan veri setlerine en uygun 
agirliklari bulmaya calisirlar, bu ise istedigimiz bir sey degil.
Elimdeki veri setinin dogru degerlerini bulmaya degil gelecegi tahmin
etmeye calisiyorum. Bu yüzden eger grafikte belli bir yerden sonra loss'larin
ve val_loss'larin ayrildigini goruyorsam overfitting yapiyorum. epochs'u
azaltmam lazim.
"""
from sklearn.metrics import mean_absolute_error, mean_squared_error

tahminDizisi = model.predict(x_test)
""" print(tahminDizisi) 
array([[22932.852],
       [23579.229],
       [24743.682],
       ...,
       [26146.795],
       [12069.229],
       [24614.72 ]], dtype=float32)

Tahmin dizisinin icersinde belirli fiyatlar var. 
y_test icersinde bunun dogru karsiliklari var
"""        

mean_absolute_error(y_test, tahminDizisi) 
"""  3204.2584571280418 pound'luk absolute fark var
bizim mean price = 24074 kusur, yani bu fiyattan 3204 sapabilir
(3204/24074)*100 = %13'luk fark var. %13'luk fark buyuk bir fark aslinda  

Napabiliriz : 1- Geri donup veriyi degistirebiliriz, temizleyebiliriz
2- test_size'i degistirebilirizi epochs'u arttirabiliriz
3- Noron ve katman sayisini degistirebiliriz
4- Ama overfitting'e dikkat edilmeli
"""
mean_squared_error(y_test, tahminDizisi) # 19996661.74594163  

plt.scatter(y_test, tahminDizisi) # grafikte cok garip bir durum yok
plt.plot(y_test, y_test, "y-*")
# üstteki ikisini komut satirinda okut,

#---- 2.indexteki satiri alip, o satiri deneyerek 
# yeni bir fiyat bulalım. Ne kadar saptı? 

dataFrame["price"].iloc[2]
# 65980

yeniArabaSeries1 = dataFrame.drop("price", axis=1).iloc[2]

yeniArabaSeries = scaler.transform(yeniArabaSeries1.values.reshape(-1,5))

model.predict(yeniArabaSeries) 
#array([[61615.867]], dtype=float32)


























