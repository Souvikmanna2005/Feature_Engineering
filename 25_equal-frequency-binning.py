import pandas as pd
df=pd.DataFrame({
    'Value':[5,12,18,25,32,45,55,63,75,89]
})
print(df)
df['Equal_Freq_Bin']=pd.qcut(df['Value'],q=4)
print(df)