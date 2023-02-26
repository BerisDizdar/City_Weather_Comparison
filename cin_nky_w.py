#Python packages
import pandas as pd 
import numpy as np 

#DataFrame
df_cin_nky_w = pd.read_csv('Weather_Data-Cinci_NKY_Weather.csv') 

#Visualizing Data
df_cin_nky_w.head(15) 
column_list = df_cin_nky_w.columns
data_types = df_cin_nky_w.dtypes

#Variables 
#date = df_cin_nky_w['DATE'] 
min_temp = df_cin_nky_w['TMIN'] 
max_temp = df_cin_nky_w['TMAX'] 
snow_fall = df_cin_nky_w['SNOW'] 
rain_fall = df_cin_nky_w['PRCP']

#Renaming Columns
df_cin_nky_w.rename(columns = {'NAME': 'LOCATION'}, inplace= True)
df_cin_nky_w.rename(columns = {'TMIN': 'LOW'}, inplace = True)
df_cin_nky_w.rename(columns = {'TMAX': 'HIGH'}, inplace = True) 
df_cin_nky_w.rename(columns = {'PRCP': 'PRECIPITATION'}, inplace = True)  

#print(df_cin_nky_w['DATE'].str.replace('-', '/'))  #Need to fix, how to make change permanant?   

#Remove Columns
df_cin_nky_w.drop(columns = ['LATITUDE', 'LONGITUDE'], inplace = True)  

Jan_data = df_cin_nky_w[0:31]
Feb_data = df_cin_nky_w[31:59]
Mar_data = df_cin_nky_w[59:90] 
Apr_data = df_cin_nky_w[90:120]
May_data = df_cin_nky_w[120:151]
Jun_data = df_cin_nky_w[151:181]
Jul_data = df_cin_nky_w[181:212]
Aug_data = df_cin_nky_w[212:243]
Sep_data = df_cin_nky_w[243:273]
Oct_data = df_cin_nky_w[273:304]
Nov_data = df_cin_nky_w[304:334]
Dec_data = df_cin_nky_w[334:365]


Jan_temp_high = Jan_data['HIGH'].max(), Jan_data['HIGH'].median(), Jan_data['HIGH'].min(), Jan_data['HIGH'].mean()  
Jan_temp_low = Jan_data['LOW'].max(), Jan_data['LOW'].median(), Jan_data['LOW'].min(), Jan_data['HIGH'].mean()  
#print(Jan_temp_low, Jan_temp_high) 
Jan_precip = Jan_data['PRECIPITATION'].sum()

#print(Jan_precip, 'inches') 
Jan_snow = Jan_data['SNOW'].sum()
#print(Jan_snow, 'inches') 

print(Jan_temp_low) 