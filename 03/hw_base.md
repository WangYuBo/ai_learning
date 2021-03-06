1. 画图解释图像卷积滤波的基本原理,并进一步简述常见图像平滑滤波算法.

![移动卷积核,使得敏感点变平](https://github.com/WangYuBo/ai_learning/03/hw_01_01.jpg)

用数学公式简述最方便,
 
 ![数学公式](https://github.com/WangYuBo/ai_learning/03/hw_01_02.png)

f(x,y)是原图像,通过与卷积核g(x,y)进行卷积运算,操作图像中的像素.常见均值滤波/加权平均滤波/中值滤波/高斯滤波/图形图像学滤波.
如果是给按照卷积核大小,给原图像覆盖范围内像素取均值,就是均值滤波.卷积核中值不一样,比如四邻域/八邻域/九邻域.会影响图像表现.均值滤波处理后图像大小不变.
如果卷积核是不同权重,就是加权平均滤波.如果是中间权重最高,周边权重低,则是高斯滤波.
中值滤波是确定卷积核窗口及位置,把窗口内像素个数顺序排列,取中间值,代替原窗口中心像素值.中值滤波处理椒盐噪声很有效.

图形图像学滤波是根据卷积核中锚定点,按照膨胀或者腐蚀,处理原图像.如果是膨胀,最后取并集,得到新图像.如果是腐蚀,最后取交集,得到最终图像.

2. 简述边缘检测基本原理,以及Sobel/LoG/Canny算子的原理及差异;

答:边缘检测基本原理使用高通滤波检测边缘.图像灰度不同,灰度的一阶微分曲线会有极值点,二阶微分曲线会有零点,代表着图像灰度的变化极值点,也就是边缘.图像在x/y方向的二阶微分,即展示出了图像灰度变化,边缘就是二阶微分指向的原函数极值点集合.

边缘检测就是差分,差分就是高通滤波.如果x/y方向上是高通滤波,那么x/y系数之和为零 .

Robert算子基本原理是在x/y方向上,用2*2算子卷积核,进行差分计算,得到边缘.
Sobel算子是使用一阶差分,3*3算子卷积核,进行差分计算.
Laplace算子是使用二阶差分模板,5*5算子卷积核,该卷积核像倒过来的墨西哥草帽.二阶差分对噪声敏感,处理噪声效果不好.
LoG算子先使用高斯滤波去除噪声,再使用Laplace算子检测边缘.

Canny算子有去除噪声/检测稳健/能连通弱连接等优点.原理是分四步:

    1. 先预处理图像,使用高斯函数平滑图像,同时计算微分;
    2. 设置极小阀值与极大阀值.通过比较山脊像素点,找到唯一确定点,在4个方向上梯度计算幅值和方向;
    3. 进行非极大值抑制,消除虚假边缘;
    4. 连通弱连接;

3. 简述图像直方图基本原理,大津算法进行图像分割的基本原理;

答:图像直方图是图像中各个像素点的灰度分布统计.大津算法假设目标与背景灰度是二值分布,为确定最佳阈值,使用目标和背景的类间方差最大,此时二者差异最大.

> u = w0u0 + w1u1  
g = w0(u0 - u)2 + w1(u1 - u)2
g = w0w1(u0 - u1)2

因为灰度值从0到255,遍历灰度值得到最大值,即为最佳阈值,以此阈值分割目标与背景.

4. 简述Harris算子对角点定义,角点检测基本原理.说明引入角点响应函数意义.

答: Harris 算子定义一个灰度在各个方向上变化幅度最大的点.在平缓区，灰度积分基本不变；在边缘部分，灰度积分只在某一个方向上有较大变化；
在角点，灰度积分各个方向都有较大变化。角点检测就是利用卷积核检测图像灰度变化，找到这个点.角点响应函数为:
![角点响应函数公式](https://github.com/WangYuBo/ai_learning/03/hw_03_harris_funtion.png)
当R < 0时,说明点为边界像素;当R>0时说明点为角点;当R在0附近,说明在平缓区.

5. 简述Hough变换基本原理(参数空间变换/参数空间划分网格统计)

答: 检测直线时使用到了Hough变换.人类一眼就能看出直线,为什么还要检测?主要是直线在计算机看来,需要用方程解释,不同直线需要有不同的直线方程解释.另外,实际图像里,像素不一定严格在一条直线上,可能会有折角.
Hough变换基于点-线对偶思想.是把直线方程 y=kx+b (1)所在坐标系,通过参数x/y变换成另外参数:以直线与x轴夹角θ/原点到直线距离为参数.这时候它的参数方程变成了: p=xcosθ+ysinθ (2).这时候,(2)上函数的每个点,都对应 x/y坐标系的一条直线.检测直线的问题,就转变成了新坐标系里统计点的问题.

怎么统计点呢?把新坐标系里划分成单位方格,根据x-y平面每一个直线点代入p/θ坐标,算出各个p,统计每个方格里有点数.设置阈值T,格子里点数小于T,不是共线点,舍弃;大于T,这些点近似在同一条直线上.

6. 简述SIFT原理(重点是尺度空间和方向直方图原理)及ORB算子原理(重点是FAST和BRIEF)
答：
Sift算法是David Lowe于1999年提出的局部特征描述子，并于2004年进行了更深入的发展和完善。Sift特征匹配算法可以处理两幅图像之间发生平移、旋转、仿射变换情况下的匹配问题，具有很强的匹配能力。总体来说，Sift算子具有以下特性：

　　（1）Sift特征是图像的局部特征，对平移、旋转、尺度缩放、亮度变化、遮挡和噪声等具有良好的不变性，对视觉变化、仿射变换也保持一定程度的稳定性。

　　（2）独特性好，信息量丰富，适用于在海量特征数据库中进行快速、准确的匹配。

　　（3）多量性，即使少数的几个物体也可以产生大量Sift特征向量。

　　（4）速度相对较快，经优化的Sift匹配算法甚至可以达到实时的要求。

　　（5）可扩展性强，可以很方便的与其他形式的特征向量进行联合。

　　其Sift算法的三大工序为：

　　（1）提取关键点；

　　（2）对关键点附加详细的信息（局部特征）也就是所谓的描述器；

　　（3）通过两方特征点（附带上特征向量的关键点）的两两比较找出相互匹配的若干对特征点，也就建立了景物间的对应关系。提取关键点和对关键点附加详细的信息（局部特征）也就是所谓的描述器可以称做是Sift特征的生成，即从多幅图像中提取对尺度缩放、旋转、亮度变化无关的特征向量。

　　Sift特征的生成一般包括以下几个步骤：

　　（1）构建尺度空间，检测极值点，获得尺度不变性；

   （2）特征点过滤并进行精确定位
   
   （3）为特征点分配方向值；
   
   （4） 计算变换参数
    当两幅图像的Sift特征向量生成以后，下一步就可以采用关键点特征向量的欧式距离来作为两幅图像中关键点的相似性判定度量。取图1的某个关键点，通过遍 历找到图像2中的距离最近的两个关键点。在这两个关键点中，如果次近距离除以最近距离小于某个阙值，则判定为一对匹配点。

    二、Surf算法原理
 不会。。