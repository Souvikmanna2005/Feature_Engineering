import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data= {
    'Name':['Ram','Sudev',np.nan,'Ankit','Rita','Golam',np.nan,'Rita'],
    'Age':[64,26,35,np.nan,38,42,np.nan,42],
    'Height':[152,np.nan,135,142,np.nan,157,161,146],
    'Weight':[68,np.nan,75,70,82,57,43,np.nan],
    'Grade':[np.nan,'B',np.nan,'D','C','A',np.nan,'B'],
}

df=pd.DataFrame(data)
print("Original Dataset:")
print(df)

df_f=df.ffill()
df_b=df.bfill()
print("\nAfter Forward Fill")
print(df_f)
print("\nAfter Backward Fill")
print(df_b)