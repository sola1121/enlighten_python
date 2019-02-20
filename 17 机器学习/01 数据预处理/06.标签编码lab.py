import numpy as np
import sklearn.preprocessing as sp


raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota', 'ford', 'bmw', 'toyota', 'ford', 'audi'
])

label_encoder = sp.LabelEncoder()
lab_samples = label_encoder.fit_transform(raw_samples)
print(lab_samples)
raw_samples = label_encoder.inverse_transform(lab_samples)
print(raw_samples)

for val in zip(lab_samples, raw_samples):
    print(val)