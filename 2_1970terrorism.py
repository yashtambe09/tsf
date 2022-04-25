import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster
df = pd.read_csv(r"C:\Users\Tanmay Dhawale\globalterrorismdb_0718dist.csv",encoding='latin1')

print("--------------------------------------------TERRORIST ACTION IN 1970 AND AFFECTED LOCATIONS--------------------------------")
filterYear = df['iyear'] == 1970
filterData = df[filterYear] 

reqFilterData = filterData.loc[:,'city':'longitude'] 
reqFilterData = reqFilterData.dropna() 
reqFilterDataList = reqFilterData.values.tolist()
# reqFilterDataList
map = folium.Map(location = [0, 30], tiles='CartoDB positron', zoom_start=2)
# clustered marker
markerCluster = folium.plugins.MarkerCluster().add_to(map)
for point in range(0, len(reqFilterDataList)):
    folium.Marker(location=[reqFilterDataList[point][1],reqFilterDataList[point][2]], popup = reqFilterDataList[point][0]).add_to(markerCluster)
print(map)
print("84% of the terrorist attacks in 1970 were carried out on the American continent. Middle East and North Africa, currently being the centre of terrorism, in 1970,faced only one terrorist attack.")
