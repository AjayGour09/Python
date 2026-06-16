import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(current_dir, "sample_rankings_50_rows.csv")

df = pd.read_csv(csv_file)

# print(df)
print(df.loc[2]['Title'])

def ectract_episodes(txt):
    check = False
    data = ""
    for i in txt:
        if i ==")":
            break
        if i == '(':
            check == True
        if check == True:
            data +=i
    return data
print(df['Title'].apply(ectract_episodes))