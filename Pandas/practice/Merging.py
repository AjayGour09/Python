import numpy as np
import pandas as pd 

employees = pd.DataFrame({
    'employee_id' : [1,2,3,4,5],
    'name' : ['Alice', 'John','Smith', 'Peter' ,'MJ'],
    'Department' : ['HR','Finance','IT','HR','IT']
})

salaries = pd.DataFrame({
    'employee_id' : [1,2,3,6,7],
    'salary' : [65000,98000,23000,54000,78000],
    'bonus' : [5000,1000,5600,2300,8700]
})
# print(employees)
# print(salaries)

print(pd.merge(employees,salaries))
print(pd.merge(employees,salaries , on='employee_id', how='inner'))
print(pd.merge(employees,salaries , on='employee_id', how='outer'))
print(pd.merge(employees,salaries , on='employee_id', how='left'))
print(pd.merge(employees,salaries , on='employee_id', how='right'))








