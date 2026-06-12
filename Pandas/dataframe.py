import numpy as np
import pandas as pd

data = {
    'Name' :['John' , 'Anna' , 'Peter' , 'Linda'],
    'Age' :[28,34,29,42],
    'City' :['New York' ,'Paris' , 'Berlin' , 'London'],
    'salary' :['20000','40000','54000','65000']
}
print(pd.DataFrame(data))

data_list  = [
    ['john' , 28 ,'Newyork',44000],
    ['Ajay',22 , 'India' , 228000],
    ['Baiju' , 32 , 'Afgnistan', 22000],
    ['Linda',22,'Russia',220000]
]

columns = ['Name' , 'Age' , 'City' , 'Sallary']

df2 = pd.DataFrame(data_list , columns=columns)
print(df2)
print(df2['Name'])
print(df2[['Name' , 'City']])

df2['Degination'] = ["Doctor" , 'Engineer' , 'Dentist' , 'Actor']
print(df2)

print(df2.drop('Degination',axis=1 ,inplace=True))

print(df2.drop(['City' , 'Name'],axis=1 ))
print(df2.loc[0])
print(df2.loc[[1,2]])
print(df2.loc[[0,1]][["City" ,'Sallary']])
print(df2[df2['Age'] <30])
print(df2[df2['Name'] =="Ajay"])

print(df2[(df2['Age'] < 30) & (df2['Sallary'] > 50000)])