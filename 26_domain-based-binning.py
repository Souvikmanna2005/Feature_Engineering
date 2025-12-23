import pandas as pd
df=pd.DataFrame({
    'Value':[5,12,18,25,32,45,55,63,75,89]
})
print(df)
bins=[0,40,70,100]
labels=['Low','Medium','High']
df['Custom_Bin']=pd.cut(df['Value'],bins=bins,labels=labels)
print(df)

