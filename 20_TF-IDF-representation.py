#Tf-idf transform to text data

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.DataFrame({
    'Text':[
        'Cats are running quickly',
        'Dogs are barking loudly',
        'He studies in the university',
        'They are enjoying the holidays'
    ]
})

print('Original DataFrame:')
print(df)

tfidf = TfidfVectorizer()

x = tfidf.fit_transform(df['Text'])

tfidf_df = pd.DataFrame(x.toarray(),columns=tfidf.get_feature_names_out())
print('\nTF-IDF Representation:')
print(tfidf_df)