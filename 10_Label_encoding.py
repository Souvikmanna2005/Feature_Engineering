import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    'Fruit':['Apple','Banana','Orange','Apple','Banana'],
    'Color':['Red','Yellow','Orange','Green','Yellow']
}

df=pd.DataFrame(data)
print('\nOriginal Dataset:')
print(df)

label_encoder=LabelEncoder()
df_label_encoded=df.copy()
df_label_encoded['Fruit']=label_encoder.fit_transform(df['Fruit'])
df_label_encoded['Color']=label_encoder.fit_transform(df['Color'])

print('\nAfter label Encoding:')
print(df_label_encoded)