
from sklearn.preprocessing import StandardScaler


data = [[3,2],[15,6],[0,10],[1,18]]

scaler = StandardScaler()
print(scaler.fit(data))
print(scaler.mean_)
print(scaler.transform(data))