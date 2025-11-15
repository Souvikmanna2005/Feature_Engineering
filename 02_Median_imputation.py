import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

data= {
    'Age':[64,26,35,np.nan,38,42,np.nan,42],
    'Height':[152,np.nan,135,142,np.nan,157,161,146],
    'Weight':[68,np.nan,75,70,82,57,43,np.nan],
}

df=pd.DataFrame(data)
print('\nOriginal dataset...')
print(df)
imputer=SimpleImputer(strategy='median')
df_imputed=pd.DataFrame(imputer.fit_transform(df[['Age','Height','Weight']]),
                        columns=['Age','Height','Weight'])
df['Age']=df_imputed['Age']
df['Height']=df_imputed['Height']
df['Weight']=df_imputed['Weight']
print('\nafter median imputation')
print(df)