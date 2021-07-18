# 数据处理专栏（po上一些常用的数据处理代码，python or matlab）

## 1 数据变换
### 1.1 傅里叶变换
#### 1.1.1 引言
要对一个非周期且连续的函数做傅里叶变换，可以分为两步走。
1. 对这个连续函数进行`抽样`。变成离散的函数，为了最后能恢复出原信号，抽样频率要满足抽样定理。
```python
# 抽样过程
t = np.linspace(0,1,Fs)
y = np.sin(2*np.pi*f1*t)*np.exp(-t/tao)
```
2. 将这个离散函数`周期化`。然后求出其傅里叶级数，即DFT，此时求得的傅里叶级数是离散非周期傅里叶变换的抽样，这个抽样同样要满足抽样定理，也就是扩展的周期要足够大。
在具体实现的时候，并不用做周期化，因为我们调用FFT实现的就是DFT。FFT跟DFT区别只不过FFT利用傅里叶级数的特点降低了算法的时间复杂度，没有信息的丢失。
#### 1.1.2 完整代码
```python
import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt

Fs = 1024
tao = 1/4
f1 = 200

t = np.linspace(0,1,Fs) # 如果区间从（0,2），那么FFT出来频率的结果就不对。因为频率间隔不是1，而是1/2了。。
y = np.sin(2*np.pi*f1*t)*np.exp(-t/tao)
plt.subplot(121)
plt.plot(t,y)   
plt.title('initial wave')

Y = np.abs(fft(y))/Fs
half_Y = Y[range(int(Fs/2))]
plt.subplot(122)
plt.plot(half_Y)
plt.title('FFT')
```
