## 第三章 Logistic线性回归之分类

Logistic线性回归不是用在回归问题上么?怎么还可以分类?
对的,名字叫"线性回归",实际上是用来分类的.回归问题面向连续型,分类问题是离散型.在机器学习里,他们俩有相同的套路:
> 都是先特征工程,预处理好数据；查看原数据特点,数据稀疏,回归问题用Lasso模型,分类用??.
>然后训练模型,评价模型性能,调超参数,应用到新数据集上.

他们俩背后原理有什么区别呢?

Logistic等线性回归,是说用线性函数做决策面,根据线性函数,把各原始数据X按最大概率分类.比如某个x可能属于类别y1和类别y2,但y1类别可能性更大,就把x分类给y1.比如一个于场,自动按照类别可能性,把鱼挑选出来做自动分类.

回归问题,是用训练数据中的原始数据X和目标数据y,回归问题就是找出X和y有映射关系,然后用这个映射关系,预测新的数据集.比如知道了去年前年降雨量和农作物收成,就可以输入今年降雨量预测农作物收成.

回归和分类都有L1/L2损失.L2损失等价于极大似然估计,L1损失等价于拉普拉斯分布.回归问题L2损失是凸函数比较好求导,常用迭代求解法(比如随机梯度下降/平均梯度下降)和解析解求得极小值.
分类问题L2损失不能用解析解求,常用迭代法如梯度下降和牛顿法求解.Logistic L1正则函数不连续,在零点没法求导,经常用坐标轴下降法找极小值.




