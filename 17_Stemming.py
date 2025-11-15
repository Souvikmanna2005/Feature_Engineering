import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt_tab')

df = pd.DataFrame({
    'Text':[
        'Cats are running quickly.',
        'Dogs were barking loudly!',
        'He studies in university.',
        'They are enjoying the holidays.',
        'ran fast'
    ]
})

print('Original DataFrame:')
print(df)

stemmer = PorterStemmer()
def stem_text(text):
    tokens = word_tokenize(text.lower())
    stems = [stemmer.stem(word) for word in tokens if word.isalpha()]
    return" ".join(stems)

df['Stemmed_Text'] = df['Text'].apply(stem_text)

print('\nAfter Stemming:')
print(df[['Text','Stemmed_Text']])