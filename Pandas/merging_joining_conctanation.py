import numpy as np

import pandas as pd

employes = pd.DataFrame(
    {
        'employee_Id' : [1,2,3,4,5],
        'name' : ['Ajay','Vinode' , 'Rustam' , 'Sahil' ,'Vedant'],
        'Department' : ['software' , 'IT' , 'HR' , 'Support', 'HR']
    }
)
salary =pd.DataFrame({
    'employee_Id' :[1,4,6,4,3],
    'Salary' :[20000,40000,32000,12000,76000],
    'Bonus' :[1000,12000,600,6500,1200]
})
print(employes)
print(salary)
merge = pd.merge(employes , salary , on='employee_Id', how='inner')
merge = pd.merge(employes , salary , on='employee_Id', how='outer')
merge = pd.merge(employes , salary , on='employee_Id', how='left')


df1 = pd.DataFrame({
    'name':['Alice', 'Bob','Joe']
    
}, index=[1,2,3])

df2 = pd.DataFrame({
    'Score':[85,90,75]
}, index=[2,3,4])
print(df2)
print(df1.join(df2))
print(df1.join(df2,how='outer'))