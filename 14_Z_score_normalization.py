import numpy as np

data = np.array([200,300,400,600,1000])

mean = np.mean(data)

std_dev = np.std(data)

z_scores = (data-mean) / std_dev

print('Original data:',data)

print('Mean:',mean)

print('Standard Deviation:',std_dev)

print('Z-scores:',z_scores)