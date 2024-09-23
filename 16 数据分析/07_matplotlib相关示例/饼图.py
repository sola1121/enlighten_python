import matplotlib.pyplot as plt

plt.figure('Pie', facecolor='lightgray')
plt.title('Pie', fontsize=20)

plt.pie(
    [26, 17, 21, 29, 11],   # 值列表
    [0.05, 0.01, 0.01, 0.01, 0.01],   #间隙列表
    ['Python', 'JavaScript', 'C++', 'C', 'PHP'],   # 标签
    ['dodgerblue', 'orangered', 'limegreen',
     'violet', 'gold'],
    '%d%%', shadow=True, startangle=90)  # 阴影, 开始角度

plt.axis('equal')   # 等轴的效果, 让饼子更圆

plt.show()
