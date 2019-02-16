import random
import matplotlib.pyplot as plt
import time
sozluk = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
i=0
while i <= 1000:
    x = str(random.randint(0,9))
    if x in sozluk:
        sozluk[x] = sozluk[x] + 1
    else:
        pass
    plt.bar(range(len(sozluk)), list(sozluk.values()), align='center',color=(0.2, 0.4, 0.6, 0.8))
    plt.xticks(range(len(sozluk)), list(sozluk.keys()))
    plt.ylabel("Sıklık")
    plt.xlabel('Sayılar')
    plt.title('Frekans Grafiği')
    plt.pause(0.01) #time for wait every loop
    i = i+1

plt.show()