import sklearn.datasets as sd
import matplotlib.pyplot as plt


faces = sd.fetch_olivetti_faces("../data")

x = faces.data
y = faces.target
print(x.shape)

plt.figure("Olivetti Faces", facecolor="black")
plt.subplots_adjust(left=0.04, bottom=0, right=0.98, top=0.96, wspace=0, hspace=0)   # 多张子图, 上下左右边距, 水平垂直间距

rows, cols = 10, 40
for row in range(rows):
    for col in range(cols):
        plt.subplot(rows, cols, row * cols + col + 1)
        plt.title(str(col), fontsize=8, color="limegreen")
        if col == 0:
            plt.ylabel(str(row), fontsize=8, color="limegreen")
            plt.xticks(())
            plt.yticks(())
            image = x[y == col][row].reshape(64, 64)
            plt.imshow(image, cmap="gray")

plt.show()
