import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
data=pd.DataFrame({
    'x1':[2,4,6,3,5],
    'x2':[3,5,7,8,10]
})
print("Original Data:")
print(data)
poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(data)
feature_names = poly.get_feature_names_out(['x1', 'x2'])
poly_df = pd.DataFrame(poly_features, columns=feature_names)
print('\npolynomial + interaction features:')
print(poly_df)