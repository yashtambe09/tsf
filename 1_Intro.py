import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster
df = pd.read_csv(r"C:\Users\Tanmay Dhawale\globalterrorismdb_0718dist.csv",encoding='latin1')
print(df.head())

print("----------------------------------: CONCISE SUMMARY OF DATAFRAME :-----------------------------------------------------")
print(df.info())


print("----------------------------------: ANALYZING THE COLUMNS AND WHOLE DATASET :-----------------------------------------------------")
print(df.describe())


print("----------------------------------: FINDING CO-RELATION OF DATAFRAMES-----------------------------------------------------")
print(df.corr())


print("----------------------------------: COLUMNS IN THE DATAFRAME :-----------------------------------------------------")
print(df.columns)



# print("-----------------------------------------US Terror Attacks and Death Injuries-------------------------------------------------------------------------------")

df.nkillus.plot(kind = 'line', color = 'red', label = 'TOTAL DEATHS IN US', linewidth = 2, alpha = 0.8, grid = True, 
                 linestyle = ':', figsize = (20,20), fontsize=15)
df.nwoundus.plot(color = "green", label = 'TOTAL NON-FATAL CONFIRMED INJURIES', linewidth = 2, alpha = 0.8, grid = True, 
                 linestyle = '-.', figsize = (20,20), fontsize=15)



plt.legend(loc='upper right')    
plt.xlabel('Database Index', fontsize=10)           
plt.ylabel('TOTAL DEATHS OR INJURIES', fontsize=15)
plt.title('TOTAL DEATHS AND NON-FATAL INJURIES IN UNITED STATES')         
plt.show()
print("CONCLUSION: Given that the data is sorted by dates, attacks on US citizens seem to be very rare in a given date range. But the terrorist act against the citizens of US has been increasingly in the following year after this rare date range. By finding the date of the start of the increase, the factors in increasing terrorist acts can be easily identified by taking into account the changes and developments in the country after this date.")




print("----------------------------------TOTAL DEATHS AND INJURIES OF ALL TIME-SPAN-----------------------------------------------------")

df.plot(kind = 'scatter', x = 'nkill', y = 'nwound', alpha = 0.5, color = 'red', figsize = (20,20), fontsize=15)
plt.xlabel('Kills', fontsize=15)
plt.ylabel('Woundings', fontsize=15)
plt.title('SCATTER PLOT: KILLS & WOUNDS')
plt.show()






print("-----------------------------TERRORISM ACTION IN SPECIFIC REGION-----------------------")
middleEastData = df[df['region'] == 10]
middleEastData.iyear.plot(kind = 'hist', bins = 30, figsize = (20,20), color = 'red', fontsize=15)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.title('FREQUENCY OF TERRORISM ACTION W.R.T. YEARS IN Middle East & North Africa')
plt.show()







