import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster


df = pd.read_csv(r"C:\Users\Tanmay Dhawale\globalterrorismdb_0718dist.csv",encoding='latin1')
killData = df.loc[:,'nkill']


print('--------------------->NUMBER OF PEOPLE KILLED BY TERRORIST ATTACKS', int(sum(killData.dropna())))

print("Let's look at what types of attacks these deaths were made of.")
attackData = df.loc[:,'attacktype1':'attacktype1_txt']

#data for the attacks
typeKillData = pd.concat([attackData, killData], axis=1)
typeKillFormatData = typeKillData.pivot_table(columns='attacktype1_txt', values='nkill', aggfunc='sum')


print("-----------------------------NUMBER OF PEOPLE KILLED Vs. COUNTRIES-----------------------")
countryData = df.loc[:,'country':'country_txt']

#data for all countries involved
countryKillData = pd.concat([countryData, killData], axis=1) 
countryKillFormatData = countryKillData.pivot_table(columns='country_txt', values='nkill', aggfunc='sum')
print(countryKillFormatData)