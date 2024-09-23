import matplotlib.pyplot as plt

plt.figure(facecolor="lightgray")

for row in range(2):
    for column in range(3):
        plt.subplot(2 , 3, row * 3 + column + 1)
        plt.xticks(())
        plt.yticks(())
        plt.text(0.5, 0.5, str(row)+str(column), ha="center", va="center", size=36, alpha=.5)

plt.show()