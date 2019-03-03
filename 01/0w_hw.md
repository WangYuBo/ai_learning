1. 视觉系统都有哪些构成要素? 以机械臂视觉控制系统为例，说明视觉系统的构成要素。 
答:有四个构成要素:光源/相机/主机/算法软件.机械臂视觉控制系统中,光源为室内照明或者专门光照,与机械臂固定一起的相机负责采集图像,然后通过数据线传输给主机,由算法软件处理图像,并反馈回给机械臂.

2. 尝试从模仿人类视觉处理流程的角度，阐述本对课程内容组织的理解。进一步在网上搜索，找到自己认为学习过程中最值得参考的1-2本书(不要太厚) 
答:课程架构从数学/物理层到应用基础层,再到应用层.数学/物理层包括线性代数/概率论/高等数学/最优化方法,物理层是刚性物体的运动规律.基础应用层则是图像处理和模式识别.图像处理是有数学/物理层支撑的,模式识别主要是数学层支撑.应用层是深度学习和计算机视觉,深度学习也需要模式识别及其下的数学层支撑.计算机视觉则需要深度学习/模式识别/物理共同支撑.

课程内容组织参考Marr的经典视觉计算系统.他的理论系统先将采集实物信息变成二维,再变成2 1/2维,最后变成三维,有空间和位置.课程设置先从光源和照明开始,分辨颜色和光强弱.图像预处理等,再加上特征提取/边缘检测/图像分别等,让图像初步变成二维.之后使用位姿估计/运动估计/相机标定等,从2 1/2维变三维视觉.

3. 什么是光通量和辐照度？说明几个常见光源的光通量，以及几个常见照明环境的辐照度。 
4. 结合颜色空间示意图，简述HSI颜色空间中各通道的物理意义，并结合图像实例说明。 
5. 说明彩色图像传感器及γ校正的基本原理。