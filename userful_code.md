# 数据处理专栏（po上一些常用的数据处理代码，python or matlab）

## 1 数据变换
### 1.1 傅里叶变换
```python
import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
# 参数初始化
Fs = 1024
tao = 1/4
f1 = 200

t = np.linspace(0,1,Fs) # 如果区间从（0,2），那么FFT出来频率的结果就不对，不太明白，希望有人可以告诉我。
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
