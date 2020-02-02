# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 02:59:43 2020

@author: Regaip
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

veri = pd.read_csv("Borçlar.csv",sep=";", index_col=0)

veri_2017 = veri.iloc[0:12,]
veri_2018 = veri.iloc[12:24,]
veri_2019 = veri.iloc[24:,]
plt.style("whitegrid")
plt.figure(figsize=(15,10))
plt.bar(veri.index, veri["Toplam"], label="Toplam")
plt.bar(veri.index, veri["Anapara"], label="Anapara")
plt.bar(veri.index, veri["Faiz"], label="Faiz")
plt.legend()
plt.xticks(veri.index, rotation='vertical')
plt.title("Merkezi Yönetim Dış Borç Ödemeleri", fontdict={"size":20})
plt.xlabel("Aylar ve Yıllar", fontdict={"size":15})
plt.ylabel("Ödeme Miktarı \nMilyon $", fontdict={"size":15})

#plt.margins(0.1)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.1)
plt.show()