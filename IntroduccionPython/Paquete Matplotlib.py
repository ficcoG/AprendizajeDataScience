#Paquete matplotlib

import matplotlib.pyplot as plt

fig = plt.figure(figsize = [5,5])

fig.suptitle("Cuadrados - Barras",fontsize = 16, color = "blue")

spl1 = fig.add_subplot(1,1,1)

sax = [1,2,3,4,5]
say = [1,4,9,16,25]

spl1.set_xlim(0,6)
spl1.set_ylim(0,30)

spl1.bar(sax,say)

plt.show()

