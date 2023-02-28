#Python packages
import pandas as pd 
import numpy as np 
import datetime 

#DataFrame
df_Louis_w = pd.read_csv('Louisville_Weather_CSV.csv') 

#Visualizing data
df_Louis_w.tail(15) 
column_list = df_Louis_w.columns
#print(column_list) 
data_types = df_Louis_w.dtypes 
#print(data_types) 

#Renaming columns
df_Louis_w.rename(columns = {'NAME': 'LOCATION'}, inplace = True) 
df_Louis_w.rename(columns = {'TMIN': 'LOW'}, inplace = True)
df_Louis_w.rename(columns = {'TMAX': 'HIGH'}, inplace = True) 
df_Louis_w.rename(columns = {'PRCP': 'PRECIPITATION'}, inplace = True)   

#Remove columns
print(df_Louis_w.drop(columns = ['LATITUDE', 'LONGITUDE'], inplace = True))  
 
#Monthly data
Loui_Jan_data = df_Louis_w[0:31] 
Loui_Feb_data = df_Louis_w[31:59]
Loui_Mar_data = df_Louis_w[59:90]

print(Loui_Mar_data) 
