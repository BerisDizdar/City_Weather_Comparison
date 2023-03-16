#Python packages
import pandas as pd 
import numpy as np 
import datetime 

#DataFrame
df_Louis_w = pd.read_csv('Weather_Datasets/Louisville_Weather_CSV.csv') 

#Visualizing data
df_Louis_w.tail(15) 
column_list = df_Louis_w.columns
#print(column_list) 
data_types = df_Louis_w.dtypes 
#print(data_types) 

#Renaming columns
df_Louis_w.rename(columns = {'NAME': 'LOCATION', 'TMIN': 'LOW', 'TMAX': 'HIGH', 'PRCP': 'PRECIPITATION', 'TAVG': 'AVERAGE' }, inplace = True) 

df_Louis_w['DATE'] = pd.to_datetime(df_Louis_w['DATE']) 

#Remove columns
df_Louis_w.drop(columns = ['LATITUDE', 'LONGITUDE'], inplace = True)   
 
#Monthly data visualization 
Loui_Jan_data = df_Louis_w[0:31] 
Loui_Feb_data = df_Louis_w[31:59]
Loui_Mar_data = df_Louis_w[59:90]
Loui_Apr_data = df_Louis_w[90:120]
Loui_May_data = df_Louis_w[120:151]
Loui_Jun_data = df_Louis_w[151:181]
Loui_Jul_data = df_Louis_w[181:212]
Loui_Aug_data = df_Louis_w[212:243]
Loui_Sep_data = df_Louis_w[243:273]
Loui_Oct_data = df_Louis_w[273:304]
Loui_Nov_data = df_Louis_w[304:334]
Loui_Dec_data = df_Louis_w[334:365]

#print(Loui_Dec_data) 

Loui_monthly_mean = df_Louis_w.groupby(df_Louis_w.DATE.dt.month)[['HIGH', 'LOW', 'SNOW', 'PRECIPITATION']].mean() 
#print(round(Loui_monthly_mean, 2)) 
Loui_monthly_max = df_Louis_w.groupby(df_Louis_w.DATE.dt.month)[['HIGH', 'LOW', 'SNOW', 'PRECIPITATION']].max()
#print(Loui_monthly_max) 
Loui_monthly_min = df_Louis_w.groupby(df_Louis_w.DATE.dt.month)[['HIGH', 'LOW', 'SNOW', 'PRECIPITATION']].min() 
#print(Loui_monthly_min) 
Loui_monthly_sum = df_Louis_w.groupby(df_Louis_w.DATE.dt.month)[['SNOW', 'PRECIPITATION']].sum()
#print(Loui_monthly_sum) 

Loui_monthly_avg = df_Louis_w.groupby(df_Louis_w.DATE.dt.month)[['AVERAGE']].mean() 

#print(round(Loui_monthly_avg, 2)) 

print(df_Louis_w.head())  
