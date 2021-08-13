import pandas as pd
import numpy as np
cols =  ["id","FirstName","LastName","Gender","Birthday","Status","Salary","Taxes","Department","HourlyRate","MaritalStatus","OverTime"]

#Ejercicio 1
df = pd.read_csv("Datosprocesados\data.csv", sep=';')
print(df)

#Ejercicio 2
print(df.head())

#Ejercicio 3
print(df.tail(5))

#Ejercicio 4
print(df.dtypes)

#Ejercicio 5
print(df.isnull().sum())

#Ejercicio 6
print(df.isnull().sum().sum()/df.size*100)

#Ejercicio 7

print(df.isnull().sum()/len(df)*100)

#Ejercicio 8
print(df.loc[:, pd.notnull(df).sum()>len(df)*.019])

#Ejercicio 9
df= df.dropna(subset=cols,thresh=2)
print(df)

#Ejercicio 10
df.replace({'--': 'null'})

#Ejercicio 11
df.iloc[:, 3].fillna('U', inplace=True)
print(df)

#Ejercicio 12
df.iloc[:, 8].fillna('Bench', inplace=True)
print(df)

#Ejercicio 13
df.iloc[:, 9].fillna(0,inplace=True)
df.iloc[:, 9].replace({'--': 0},inplace=True)
df['HourlyRate'].replace(to_replace=np.nan,value=df['HourlyRate'].median(),inplace = True)
df[df['HourlyRate']==df['HourlyRate'].median()]
print(df)

#Ejercicio 14
df.iloc[:, 11].replace({'1': 'NO','0': 'NO','--': 'NO'},inplace=True)
df.iloc[:, 11].fillna('NO',inplace=True)
print(df)

