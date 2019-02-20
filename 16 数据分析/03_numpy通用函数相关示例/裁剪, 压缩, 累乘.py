import numpy as np


a = np.arange(1, 10).reshape(3, 3)
print("a:", a)

b = a.clip(min=3, max=7)
print("b", b)

c = a.compress(a.ravel() > 3)
print("c", c)

d = a.compress(a.ravel() < 7).reshape(-1, 3)
print("d:", d)

e = a.compress((3 < a.ravel()) & (a.ravel() < 7))
print("e:", e)

f = a.prod()
print("f:", f)

g = 1
for elem in a.flat:
    g *= elem

print("g:", g)
h = a.cumprod()
print("h:", h)
