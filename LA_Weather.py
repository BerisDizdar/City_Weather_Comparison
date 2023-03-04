#Python packages
import pandas as pd 
import numpy as np 

#DataFrame 
df_LA_W = pd.read_csv('Los_Angeles_Weather.csv')

#Visualizing data 
df_LA_W.head()
columns_list = df_LA_W.columns
#print(columns_list) 
data_types = df_LA_W.dtypes
#print(data_types) 

#Renaming columns 
df_LA_W.rename(columns = {'NAME': 'LOCATION'}, inplace = True) 
df_LA_W.rename(columns = {'TMIN': 'LOW'}, inplace = True) 
df_LA_W.rename(columns = {'TMAX': 'HIGH'}, inplace = True) 
df_LA_W.rename(columns = {'PRCP': 'PRECIPITATION'}, inplace = True) 
df_LA_W.rename(columns = {'TAVG': 'AVERAGE'}, inplace = True) 

df_LA_W['DATE'] = pd.to_datetime(df_LA_W['DATE']) 

#Remove columns
df_LA_W.drop(columns = ['LATITUDE', 'LONGITUDE'], inplace = True)

#Monthly data visualization

LA_Jan_data = df_LA_W[0:31]
LA_Feb_data = df_LA_W[31:59] 
LA_Mar_data = df_LA_W[59:90]
LA_Apr_data = df_LA_W[90:120]
LA_May_data = df_LA_W[120:151]
LA_Jun_data = df_LA_W[151:181] 
LA_Jul_data = df_LA_W[181:212]
LA_Aug_data = df_LA_W[212:243]
LA_Sep_data = df_LA_W[243:273] 
LA_Oct_data = df_LA_W[273:304]
LA_Nov_data = df_LA_W[304:334]
LA_Dec_data = df_LA_W[334:365]

#print(LA_Dec_data) 

#Calculations
LA_monthly_mean = df_LA_W.groupby(df_LA_W.DATE.dt.month)[['HIGH', 'LOW', 'AVERAGE', 'SNOW', 'PRECIPITATION']].mean()
#print(round(LA_monthly_mean, 2)) 
LA_monthly_max = df_LA_W.groupby(df_LA_W.DATE.dt.month)[['HIGH', 'LOW', 'AVERAGE', 'SNOW', 'PRECIPITATION']].max()
#print(LA_monthly_max) 
LA_monthly_min = df_LA_W.groupby(df_LA_W.DATE.dt.month)[['HIGH', 'LOW', 'AVERAGE', 'SNOW', 'PRECIPITATION']].min()
#print(LA_monthly_min) 
LA_monthly_sum = df_LA_W.groupby(df_LA_W.DATE.dt.month)[['SNOW', 'PRECIPITATION']].sum()
#print(LA_monthly_sum) 


