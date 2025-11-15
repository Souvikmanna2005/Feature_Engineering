import pandas as pd
from category_encoders import TargetEncoder
from sklearn.preprocessing import LabelEncoder

data = {
    'Fruit':['Apple','Banana','Orange','Apple','Banana'],
    'Color':['Red','Yellow','Orange','Green','Yellow']
}

df = pd.DataFrame(data)
print('Original Dataset:')
print(df)

label_encoder = LabelEncoder()
df['fruit'] = label_encoder.fit_transform(df['Fruit'])

target_encoder = TargetEncoder()
df_target_encoded = df.copy()
df_target_encoded[['Fruit','Color']] = target_encoder.fit_transform(df[['Fruit','Color']],df['Fruit'])

print('\nAfter Target Encoding:')
print(df_target_encoded) 
