import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-np.pi, np.pi, 1000)  # 千分之 -π~π的一维数组
cos_y = np.cos(x) / 2                 # 1/2cos(x)
sin_y = np.sin(x)                     # sin(x)
xo = np.pi * 3 / 4                    # 3/4π
yo_cos = np.cos(xo) / 2               # 常量 1/2cos(3/4π)
yo_sin = np.sin(xo)                   # 常量 sin(3/4π)

plt.xlim(x.min() * 1.1, x.max() * 1.1)   # x轴取值范围
plt.ylim(sin_y.min() * 1.1, sin_y.max() * 1.1)   # y轴取值范围
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi * 3 / 4, np.pi],   # 设置x轴刻度值
          [r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])   # 设置x轴值格式
plt.yticks([-1, -0.5, 0.5, 1])   # 设置y轴刻度值

ax = plt.gca()   # 获取当前轴线对象
ax.spines['left'].set_position(('data', 0))  # 移动指定位置轴线
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')   # 设置指定轴线颜色
ax.spines['top'].set_color('none')

plt.plot(x, cos_y, linestyle='-', linewidth=2, color='dodgerblue', label=r'$y=\frac{1}{2}cos(x)$')
plt.plot(x, sin_y, linestyle='-', linewidth=2, color='orangered', label=r'$y=sin(x)$')
plt.plot([xo, xo], [yo_cos, yo_sin], linestyle='--', linewidth=1, color='limegreen')

plt.scatter([xo, xo], [yo_cos, yo_sin], s=60, edgecolor='limegreen', facecolor='white', zorder=3)

plt.annotate(
    r'$\frac{1}{2}cos(\frac{3\pi}{4})=-\frac{\sqrt{2}}{4}$',   # 备注文本 1/2cos(3π/4) = -√2/4
    xy=(xo, yo_cos),                                           # xy=目标位置,
    xycoords='data',                                           # xycoords=目标坐标系
    xytext=(-90, -40),                                         # xytext=文本位置
    textcoords='offset points',                                # textcoords=文本坐标系,
    fontsize=14,                                               # fontsize=字体大小
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2')   # arrowprops=箭头属性
    )

plt.annotate(
    r'$sin(\frac{3\pi}{4})=\frac{\sqrt{2}}{2}$',            # 备注文本   sin(3π/4) = √2/2
    xy=(xo, yo_sin),                                        # xy=目标位置
    xycoords='data',                                        # xycoords=目标坐标系
    xytext=(20, 20),                                        # xytext=文本位置
    textcoords='offset points',                             # textcoords=文本坐标系
    fontsize=14,                                            # fontsize=字体大小
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2')  # arrowprops=箭头属性
    )

plt.legend(loc='upper left')   # 图例左上角

plt.show()
