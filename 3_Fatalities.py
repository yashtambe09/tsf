import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster
df = pd.read_csv(r"C:\Users\Tanmay Dhawale\globalterrorismdb_0718dist.csv",encoding='latin1')
killData = df.loc[:,'nkill']
print('TOTAL FATALITIES IN TERRORIST ATTACK:', int(sum(killData.dropna())))

print("Let's look at what types of attacks these deaths were made of.")
attackData = df.loc[:,'attacktype1':'attacktype1_txt']

typeKillData = pd.concat([attackData, killData], axis=1)
typeKillFormatData = typeKillData.pivot_table(columns='attacktype1_txt', values='nkill', aggfunc='sum')
print(typeKillFormatData)
print(typeKillFormatData.info())