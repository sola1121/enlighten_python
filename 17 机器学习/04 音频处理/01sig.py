import os
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as plt

sample_rate, sigs = wf.read(os.path.dirname(__file__) + "/signal.wav")

print("采样率", sample_rate)
print("声场数据个数:", sigs.shape)   # 显示一个数组, 即只记录一个声道
print("采样时间时间", sigs.shape[0] / sample_rate)

sigs = sigs[:30] / 2**15
print(len(sigs), "信号个数\n", sigs)

times = np.array(len(sigs)) / sample_rate
print(len(times))


plt.figure("Audio Signal", facecolor="lightgray")
plt.title("Audio Signal", fontsize=14)
plt.xlabel("Time", fontsize=10)
plt.ylabel("Signal", fontsize=10)
plt.tick_params(labelsize=10)
plt.grid(linestyle=":")
plt.plot(times, sigs, label="signal")
plt.show()
