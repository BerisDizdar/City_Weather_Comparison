#Python packages
import pandas as pd 
import numpy as np 
import datetime
import matplotlib.pyplot as plt 

#DataFrame
df_cin_nky_w = pd.read_csv('Weather_Datasets/Weather_Data-Cinci_NKY_Weather.csv') 

#Visualizing Data
df_cin_nky_w.head(15) 
column_list = df_cin_nky_w.columns
data_types = df_cin_nky_w.dtypes

df_cin_nky_w['DATE'] = pd.to_datetime(df_cin_nky_w['DATE']) 
print(df_cin_nky_w.dtypes) 

#Variables 
#date = df_cin_nky_w['DATE'] 
min_temp = df_cin_nky_w['TMIN'] 
max_temp = df_cin_nky_w['TMAX'] 
snow_fall = df_cin_nky_w['SNOW'] 
rain_fall = df_cin_nky_w['PRCP']

#Renaming Columns
'''df_cin_nky_w.rename(columns = {'NAME': 'LOCATION'}, inplace= True)
df_cin_nky_w.rename(columns = {'TMIN': 'LOW'}, inplace = True)
df_cin_nky_w.rename(columns = {'TMAX': 'HIGH'}, inplace = True) 
df_cin_nky_w.rename(columns = {'PRCP': 'PRECIPITATION'}, inplace = True)  
df_cin_nky_w.rename(columns = {'TAVG': 'AVERAGE'}, inplace = True)'''   

#Remove Columns
df_cin_nky_w.drop(columns = ['LATITUDE', 'LONGITUDE'], inplace = True)  

#Cinci/NKY monthly data
C_NKY_Jan_data = df_cin_nky_w[0:31]
C_NKY_Feb_data = df_cin_nky_w[31:59]
C_NKY_Mar_data = df_cin_nky_w[59:90] 
C_NKY_Apr_data = df_cin_nky_w[90:120]
C_NKY_May_data = df_cin_nky_w[120:151]
C_NKY_Jun_data = df_cin_nky_w[151:181]
C_NKY_Jul_data = df_cin_nky_w[181:212]
C_NKY_Aug_data = df_cin_nky_w[212:243]
C_NKY_Sep_data = df_cin_nky_w[243:273]
C_NKY_Oct_data = df_cin_nky_w[273:304]
C_NKY_Nov_data = df_cin_nky_w[304:334]
C_NKY_Dec_data = df_cin_nky_w[334:365]

C_NKY_Jan_precip = C_NKY_Jan_data['PRECIPITATION'].sum()
C_NKY_Jan_snow = C_NKY_Jan_data['SNOW'].sum()
#print(Jan_precip, 'inches') 
#print(Jan_snow, 'inches') 
 
#Monthly calculations
C_NKY_monthly_mean = df_cin_nky_w.groupby(df_cin_nky_w.DATE.dt.month)[['HIGH', 'LOW', 'SNOW', 'PRECIPITATION']].mean() 
#print(round(C_NKY_monthly_mean, 2))
C_NKY_monthly_max = df_cin_nky_w.groupby(df_cin_nky_w.DATE.dt.month)[['HIGH', 'LOW', 'SNOW', 'PRECIPITATION']].max() 
#print(C_NKY_monthly_max) 
C_NKY_monthly_min = df_cin_nky_w.groupby(df_cin_nky_w.DATE.dt.month)[['HIGH', 'LOW', 'SNOW', 'PRECIPITATION']].min()
#print(C_NKY_monthly_min) 
C_NKY_monthly_sum = df_cin_nky_w.groupby(df_cin_nky_w.DATE.dt.month)[['SNOW', 'PRECIPITATION']].sum() 
#print(C_NKY_monthly_sum) 

C_NKY_monthly_avg = df_cin_nky_w.groupby(df_cin_nky_w.DATE.dt.month)[['AVERAGE']].mean() 
#print(round(C_NKY_monthly_avg, 2))

C_NKY_monthly_mean2 = df_cin_nky_w.groupby(df_cin_nky_w.DATE.dt.strftime('%B'))[['HIGH']].mean()  
#print(round(C_NKY_monthly_mean2, 2)) 

print(C_NKY_monthly_mean2.sort_values('DATE'))

axis1 = C_NKY_Aug_data['HIGH'] 
#print(axis1) 
axis2 = C_NKY_Dec_data['LOW'] 
#print(axis2) 

#print(plt.plot(axis1, axis2, 'o'))  

#Histogram Graph
'''plt.figure(figsize = (12, 6))
plt.plot(C_NKY_monthly, bins = 15, rwidth = 0.8)
plt.xlabel('temp')
plt.ylabel('frequency') 
#print(plt.show())'''

'''plt.plot(C_NKY_monthly_mean2, 'o')
plt.xlabel('Max Median Min Mean')
plt.ylabel('High Temperature') 
#print(plt.show())''' 

df_cin_nky_w.head()
