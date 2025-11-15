import pandas as pd
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt_tab')

df = pd.DataFrame({
    'Text':[
        'Cats are running quickly.',
        'Dogs were barking loudly!',
        'He studies in university.',
        'They are enjoying the holidays.'
    ]
})

print("Original DataFrame:")
print(df)

df['Tokens']=df['Text'].apply(lambda x:word_tokenize(x.lower()))
print("\nAfter Tokenization:")
print(df[['Text','Tokens']])