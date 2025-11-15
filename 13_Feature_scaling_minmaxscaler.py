from sklearn.preprocessing import MinMaxScaler

data = [[3,2],[15,6],[0,10],[1,18]]

scaler = MinMaxScaler()
print(scaler.fit(data))

print(scaler.data_max_)
print(scaler.data_min_)

print(scaler.transform(data))