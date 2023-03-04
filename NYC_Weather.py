#Python packages
import pandas as pd 
import numpy as np 
import datetime 

#DataFrame
df_NYC_W = pd.read_csv('New_York_Weather.csv') 

#Visualizing data
df_NYC_W.head() 
column_list = df_NYC_W.columns
#print(column_list) 
data_types = df_NYC_W.dtypes
#print(data_types) 

#Renaming columns
df_NYC_W.rename(columns = {'NAME': 'LOCATION'}, inplace = True)
df_NYC_W.rename(columns = {'TMIN': 'LOW'}, inplace = True) 
df_NYC_W.rename(columns = {'TMAX': 'HIGH'}, inplace = True) 
df_NYC_W.rename(columns = {'PRCP': 'PRECIPITATION'}, inplace = True) 
df_NYC_W.rename(columns = {'TAVG': 'AVERAGE'}, inplace = True)  

df_NYC_W['DATE'] = pd.to_datetime(df_NYC_W['DATE']) 

#Remove columns 
df_NYC_W.drop(columns = ['LATITUDE', 'LONGITUDE'], inplace = True) 


#Monthly data visualization
NYC_Jan_data = df_NYC_W[0:31]
NYC_Feb_data = df_NYC_W[31:59] 
NYC_Mar_data = df_NYC_W[59:90] 
NYC_Apr_data = df_NYC_W[90:120]
NYC_May_data = df_NYC_W[120:151] 
NYC_Jun_data = df_NYC_W[151:181] 
NYC_Jul_data = df_NYC_W[181:212]
NYC_Aug_data = df_NYC_W[212:243]
NYC_Sep_data = df_NYC_W[243:273]
NYC_Oct_data = df_NYC_W[273:304]
NYC_Nov_data = df_NYC_W[304:334]
NYC_Dec_data = df_NYC_W[334:365]

#Calculations
NYC_monthly_mean = df_NYC_W.groupby(df_NYC_W.DATE.dt.month)[['HIGH', 'LOW', 'AVERAGE', 'SNOW', 'PRECIPITATION']].mean()
#print(round(NYC_monthly_mean, 2))
NYC_monthly_max = df_NYC_W.groupby(df_NYC_W.DATE.dt.month)[['HIGH', 'LOW', 'AVERAGE', 'SNOW', 'PRECIPITATION']].max() 
#print(NYC_monthly_max) 
NYC_monthly_min = df_NYC_W.groupby(df_NYC_W.DATE.dt.month)[['HIGH', 'LOW', 'AVERAGE', 'SNOW', 'PRECIPITATION']].min() 
#print(NYC_monthly_min) 
NYC_monthly_sum = df_NYC_W.groupby(df_NYC_W.DATE.dt.month)[['SNOW', 'PRECIPITATION']].sum() 
#print(NYC_monthly_sum)

print(df_NYC_W.tail())  


