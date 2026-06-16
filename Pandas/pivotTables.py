import numpy as np
import pandas as pd

data = {
    'Date': pd.date_range('2023-10-03', periods=20),
    
    'Products': ['A', 'B', 'C', 'D'] * 5,
    
    'Region': [
        "East", "West", "North", "South",
        "East", "West", "North", "South",
        "East", "West", "North", "South",
        "East", "West", "North", "South",
        "East", "West", "North", "South"
    ],
    
    'Sales': np.random.randint(100, 200, 20),
    
    'Units': np.random.randint(10, 100, 20),
    
    'Rep': [
        'Alice', 'Bob', 'Joe', 'Advert',
        'Lucas', 'Promon', 'Alice', 'Bob',
        'Joe', 'Advert', 'Lucas', 'Promon',
        'Alice', 'Bob', 'Joe', 'Advert',
        'Dhilo', 'Alice', 'Bob', 'Joe'
    ]
}

df = pd.DataFrame(data)

df['Month'] = df['Date'].dt.month_name()
df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)

print(df)

print(pd.pivot_table(df,values="Sales", index="Region",columns="Products"))