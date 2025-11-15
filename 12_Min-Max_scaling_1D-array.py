import numpy as np

data = np.array([200,300,400,600,1000])

min_val = np.min(data)
max_val = np.max(data)

scaled_data = (data-min_val) / (max_val - min_val)

print('Original data:',data)
print('Scaled data:',scaled_data)