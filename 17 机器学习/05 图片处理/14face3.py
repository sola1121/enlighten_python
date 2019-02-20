import sklearn.datasets as sd
import sklearn.decomposition as dc
import matplotlib.pyplot as plt


faces = sd.fetch_olivetti_faces("../data")

y = faces.data
x = faces.target

ncps  