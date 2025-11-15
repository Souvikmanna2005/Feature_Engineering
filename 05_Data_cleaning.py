import pandas as pd

data = {
    'A':[1,2,3,None,5],
    'B':[None,2,3,4,5],
    'C':[1,2,None,None,5]
}

df = pd.DataFrame(data)
print('\nOriginal Data:\n',df)

df_cleaned = df.dropna()
print('\nCleaned Data:\n',df_cleaned)