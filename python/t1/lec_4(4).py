import pandas as pd
import numpy as np

df = pd.read_csv("car_data.csv")
# print(df)



ritzCar = df[(df['Car_Name'] == 'ritz') & (df['Kms_Driven'] > 30000)]
# print(ritzCar.shape[0])


Petrol_cars = df[(df['Year'] == 2017) & (df['Selling_Price'] > 10) & (df['Fuel_Type'] == 'Petrol')]
# print(Petrol_cars.shape[0])



Swift_cars = df[(df['Selling_Price'] < 4) & (df['Car_Name'] == 'swift')]
# print(Swift_cars.shape[0])



Automatic_Transmission = df[(df['Fuel_Type'] == 'Petrol') & (df['Year'] == 2015) & (df['Selling_Price'] > 10)]
# print(Automatic_Transmission.shape[0])




Automatic_Transmission_count = df[(df['Transmission'] == 'Automatic') & (df['Selling_Price'] < 1)]
# print(Automatic_Transmission_count)





