import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

data= {
    'Name':['Ram','Sudev',np.nan,'Ankit','Rita','Golam',np.nan,'Rita'],
    'Age':[64,26,35,np.nan,38,42,np.nan,42],
    'Height':[152,np.nan,135,142,np.nan,157,161,146],
    'Weight':[68,np.nan,75,70,82,57,43,np.nan],
    'Grade':['A','B',np.nan,'D','C','A',np.nan,'B'],
}

df=pd.DataFrame(data)
print('\nOriginal Dataset')
imputer=SimpleImputer(strategy='most_frequent')
df_imputed=pd.DataFrame(imputer.fit_transform(df[['Name','Age','Height','Weight','Grade']]),
                        columns=['Name','Age','Height','Weight','Grade'])
df['Name']=df_imputed['Name']
df['Age']=df_imputed['Age']
df['Height']=df_imputed['Height']
df['Weight']=df_imputed['Weight']
df['Grade']=df_imputed['Grade']
print('\nAfter most_frequent imputation')
print(df)