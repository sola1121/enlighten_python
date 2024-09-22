import numpy as np

arr = np.random.randint(10, 100, 9).reshape(3, 3)
arr2 = np.random.randint(10, 100, 9).reshape(3, 3)

print(arr)

print("最大值", np.max(arr), arr.max())
print("最小值", np.min(arr), arr.min())

print("最大值所在下标", np.argmax(arr), arr.argmax())
print("最小值所在下标", np.argmin(arr), arr.argmin())


print("合体最大值列表:\n", np.maximum(arr, arr2))
print("合体最小值列表:\n", np.minimum(arr, arr2))
