import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sbn

dataFrame = pd.read_excel("maliciousornot.xlsx")

dataFrame.corr()
dataFrame.corr()["Type"].sort_values()

sbn.countplot(x= "Type", data= dataFrame)
# 0 zararsiz, 1 zararli site

dataFrame.corr()["Type"].sort_values().plot(kind="bar")

y = dataFrame["Type"].values
x = dataFrame.drop("Type", axis=1).values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=15)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout # Dropout'u overfitting icin kullanicaz
from tensorflow.keras.callbacks import EarlyStopping
"""
 # ------------------ OVERFITTIN ICIN --------------------------------

model = Sequential()

# x_train.shape  ->  (383, 30)
model.add(Dense(units= 30, activation="relu"))
model.add(Dense(units= 15, activation="relu"))
model.add(Dense(units= 15, activation="relu"))

model.add(Dense(units= 1, activation="sigmoid")) # sigmoid 0 ile 1 arasinda bir deger veriyor
# siniflandirma problemlerinde output layer'ina sigmoid aktivasyonunu kullanarak elde edilebilir

model.compile(optimizer= "adam", loss="binary_crossentropy") # siniflandirma islemi -> 0 ile 1 islemi (Binary islem) yapiyoruz
# bu yüzden loss fonksiyonunu  binary_crossentropy  kullaniyoruz

model.fit(x=x_train, y=y_train, epochs=700, validation_data=(x_test,y_test),verbose=1)
# epochs=700 cok buyuk sectim.

model.history.history 

modelKaybi = pd.DataFrame(model.history.history)
modelKaybi.plot()
"""
 
"""
validation_loss sacma sapan artmaya baslarsa durdur artık epochs'u, sen gelmissin
sonuna bu isin. Bunun demek icin EarlyStopping mekanizmasini kullanmamiz gerekiyor

"""
# --------------------------- EarlyStopping --------------------------------

#model = Sequential()


#model.add(Dense(units= 30, activation="relu"))
#model.add(Dense(units= 15, activation="relu"))
#model.add(Dense(units= 15, activation="relu"))

#model.add(Dense(units= 1, activation="sigmoid"))

#model.compile(optimizer= "adam", loss="binary_crossentropy")

early_stopping =  EarlyStopping (monitor= "val_loss", mode="min", patience=25, verbose=1)
# val_loss' u minimumda tutmaya calis
# patience=25, 25 epochs sonrası modelde herhangi bir iyilestirme yok ise durdur.

# model.fit(x=x_train, y=y_train, epochs=700, validation_data=(x_test,y_test),verbose=1, callbacks=[early_stopping])

#modelKaybi = pd.DataFrame(model.history.history)
#modelKaybi.plot()


# Hala Memnun degilsek  -> Dropout

# --------------------------- Dropout --------------------------------
model = Sequential()


model.add(Dense(units= 30, activation="relu"))
model.add(Dropout(0.6))

model.add(Dense(units= 15, activation="relu"))
model.add(Dropout(0.6))

model.add(Dense(units= 15, activation="relu"))
model.add(Dropout(0.6))

model.add(Dense(units= 1, activation="sigmoid"))

model.compile(optimizer= "adam", loss="binary_crossentropy")

model.fit(x=x_train, y=y_train, epochs=700, validation_data=(x_test,y_test),verbose=1, callbacks=[early_stopping])

kayipDf = pd.DataFrame(model.history.history)
kayipDf.plot()

tahminlerimiz = model.predict_classes(x_test)

from sklearn.metrics import classification_report, confusion_matrix
classification_report (y_test, tahminlerimiz)






