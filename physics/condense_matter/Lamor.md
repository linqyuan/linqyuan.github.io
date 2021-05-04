```
证明拉莫尔进动频率为γB的两种方法
```
## 1 经典方法
磁场产生的力矩为
$$
\boldsymbol{M}=\boldsymbol{\mu }\times \boldsymbol{B}=\gamma \boldsymbol{J}\times \boldsymbol{B}
$$
$$
M=J\gamma B\sin \theta 
$$
由牛顿第二定律的力矩形式
$$
\boldsymbol{M}=\frac{d\boldsymbol{J}}{dt}
$$
可得角动量的变化垂直于角动量，证明只是方向改变，大小不变。
$$
d\boldsymbol{J}=\boldsymbol{M}dt\bot \boldsymbol{J}
$$
拉莫尔进动频率为
$$
\varOmega =\frac{d\varTheta}{dt}
$$
由图像分析可知
![进动示意图](https://upload-images.jianshu.io/upload_images/17501363-06890a212350d026.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

$$
M=\frac{|d\boldsymbol{J}|}{dt}=\frac{J\sin \theta d\varTheta}{dt}=J\sin \theta \varOmega 
$$
最终得到
$$
\varOmega =\frac{M}{J\sin \theta}=\gamma B
$$
## 2 量子方法（只考虑自旋进动）
### (1) 两态系统在Bloch球中的表示
任何两态系统都可以表示为
$$
|\psi \rangle =c_0|0\rangle +c_1|1\rangle =|c_0|e^{i\phi _1}|0\rangle +|c_1|e^{i\phi _2}|1\rangle =e^{i\gamma}\left( \cos \frac{\theta}{2}e^{-i\frac{\phi}{2}}|0\rangle +\sin \frac{\theta}{2}e^{i\frac{\phi}{2}}|1\rangle \right) 
$$
其中，
$$
|c_0|=|\cos \frac{\theta}{2}|\text{，}|c_1|=|\sin \frac{\theta}{2}|\text{，}\varDelta \phi =\phi _2-\phi _1=\phi 
$$
这种替换没有丢掉任何信息。
$$\begin{aligned}
\\
\rho &=|\psi \rangle \langle \psi |=\left( \begin{matrix}
	\cos ^2\frac{\theta}{2}&		\sin \frac{\theta}{2}\cos \frac{\theta}{2}e^{-i\phi}\\
	\sin \frac{\theta}{2}\cos \frac{\theta}{2}e^{i\phi}&		\cos ^2\frac{\theta}{2}\\
\end{matrix} \right) 
\\
&=\frac{1}{2}\left( I+\sigma _x\sin \theta \cos \phi +\sigma _y\sin \theta \sin \phi +\sigma _z\cos \theta \right) 
\\
&=\frac{I+\boldsymbol{\sigma }\cdot \boldsymbol{n}}{2}
\end{aligned}$$
可以看出，`系统的状态可以由Bloch球中的单位向量`$\boldsymbol{n}=\left( \sin \theta \cos \phi ,\sin \theta \sin \phi ,\cos \theta \right) $表示。

由该单位向量在z轴的投影容易反推出处于哪种状态的概率。

ps：若推广到混合系综，总的密度算符为纯态密度算符的系综平均。
$$
\rho =\frac{I+\boldsymbol{\sigma }\cdot \boldsymbol{r}}{2}\text{，}\boldsymbol{r}\in \mathbb{R}^3\text{，}|\boldsymbol{r}|\leqslant 1
$$
### (2)密度算符随时间的演化
系统哈密顿量为
$$
H=-\boldsymbol{\mu }\cdot \boldsymbol{B}=-\gamma \boldsymbol{J}\cdot \boldsymbol{B}=-\gamma J_zB
$$
由薛定谔方程
$$
i \hbar\frac{\partial |\psi \left( t \right) \rangle}{\partial t}=H|\psi \left( t \right) \rangle 
$$
当哈密顿量不含时，可得态的时间演化为
$$
|\psi \left( t \right) \rangle =e^{-\frac{i}{\hbar}Ht}|\psi \left( 0 \right) \rangle 
$$
其中，时间演化算符为
$$
e^{-\frac{i}{ \hbar}Ht}=e^{\frac{i}{\hbar}J_z\gamma Bt}=e^{\frac{i}{\hbar}J_z\varOmega t}
$$
因此，密度算符为
$$\begin{aligned}
\rho \left( t \right) &=|\psi \left( t \right) \rangle \langle \psi \left( t \right) |=e^{\frac{i}{\hbar}J_z\varOmega t}\rho \left( 0 \right) e^{-\frac{i}{\hbar}J_z\varOmega t}
\\
&=\frac{1+e^{\frac{i}{\hbar}J_z\varOmega t}\boldsymbol{\sigma }e^{-\frac{i}{\hbar}J_z\varOmega t}\cdot \boldsymbol{n}\left( 0 \right)}{2}
\\
&=\frac{1+R_z\left( \varOmega t \right) \boldsymbol{\sigma }\cdot \boldsymbol{n}\left( 0 \right)}{2}
\\
&=\frac{1+\boldsymbol{\sigma }\cdot \boldsymbol{n}\left( t \right)}{2}
\end{aligned}$$
其中，$\boldsymbol{n}\left( t \right) =R_z\left( \varOmega t \right) \boldsymbol{n}\left( 0 \right) $，在Bloch球中绕z轴旋转的矩阵为
$$
R_z\left( \varOmega t \right) =\left( \begin{matrix}
	\cos \varOmega t&		-\sin \varOmega t&		0\\
	\sin \varOmega t&		\cos \varOmega t&		0\\
	0&		0&		1\\
\end{matrix} \right) 
$$
因此，从两态系统来看，磁场对自旋的作用同样是以`拉莫尔频率`$\gamma B$绕着磁场方向进动。
