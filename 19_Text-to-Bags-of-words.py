import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.DataFrame({
    'Text': [
        'Cats are running quickly.',
        'Dogs are barking loudly!',
        'They study in university.',
        'They are running to reach the target'
    ]
})

print('Original DataFrame:')
print(df)

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(df['Text'])

bow_df = pd.DataFrame(x.toarray(),columns=vectorizer.get_feature_names_out())
print('\nBag-of-words Representation:')
print(bow_df)