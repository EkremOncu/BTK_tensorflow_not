import numpy as np
import matplotlib.pyplot as plt
"""
a = np.array([10, 20, 65.5, "sadas"])
print(a)

liste = [0, 6, 12, 36, 13]
nop = np.array(liste)
print(nop)   

a = np.arange(0,10,2)
print(type(a))
print("")

b = np.zeros(5)
print(b)
print("")
b = np.zeros((4,4))
print(b)
print("")
c = np.ones((5,5))
print(c) 
"""

# linspace / eye / random
"""
a = np.linspace(0,99,100)
print(a)
# eye
print("")
b = np.eye(7)
print(b) 
print("")
# random
c = np.random.randn(4) 
print(c)
print("")
s = np.random.randn(4,3) 
print(s)
print("")
d = np.random.randint(4,13) 
print(d)
print("")
r = np.random.randint(1,59,9) 
print(r) 
"""
# Min / Max 
"""
numpyDizi = np.arange(0,30)
randomDizi = np.random.randint(0,52,24)

a = numpyDizi.reshape(6,5)
print(a)
print("")
print(a[2])
print("")

print(randomDizi)
print("")
print(randomDizi.argmax()) # dizideki en kücük sayının indexi
print(randomDizi.argmin()) 
"""
# Slice 
"""
dizi = np.arange(0,13)
print(dizi)
dizi[2:6] = [0,5,42,36] # [1, 2, 3, 4, 5, 6, 7] bu olmuyor np de
print(dizi)
print("")

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(a)
a[2:6] = [1, 2, 3, 4, 5, 6, 7]
print(a) 
"""

"""
diz = np.random.randint(0,31,20)
print(diz)
print("")
yenidizi = diz > 12
print(yenidizi)
print("")
son = diz[yenidizi]
print(son) 
"""


#  ------------------- Matplotlip ------------------------
"""        
liste = [0, 6, 12, 36, 13]
nop = np.array(liste)
print(nop)    
hop = [5, 32, 64, 74, 89]
art = np.array(hop)
print(art)

plt.subplot(1,2,1)
plt.plot(nop, art, "b*-")

plt.subplot(1,2,2) # 1 satir, 2 kolon, 2. grafik ciziliyor
plt.plot(art, nop, "r--")
plt.show()
"""

# ic ice grafik
"""
liste = [0, 6, 12, 36, 13]
nop = np.array(liste)

hop = [5, 32, 64, 74, 89]
art = np.array(hop)

figure2 = plt.figure()
eksen1 = figure2.add_axes([0.1, 0.1, 0.7, 0.7])
eksen2 = figure2.add_axes([0.2, 0.4, 0.2, 0.3])

eksen1.plot(art, nop, "r--")
eksen2.plot(art, nop, "b-*")
plt.show()   
"""

""" ????????????????
hop = [5, 32, 64, 74, 89]
art = np.array(hop)
abc = art ** 3

benimFigure, benimEksen = plt.subplots()

#benimEksen.plot(hop, abc, color="#3A95A8")
benimEksen.plot(abc, hop, "b")
plt.show()   
"""

# scatter  and  histogram
"""
hop = np.random.randint(0,350,45)
print(hop)
abc = hop ** 3
plt.scatter (hop, abc)
plt.show()

plt.hist(hop)
plt.show() 

"""










