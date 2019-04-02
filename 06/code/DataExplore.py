# -*- coding:utf-8 -*-
import pandas as pd  #
import seaborn as sns

import matplotlib.pyplot as plt

dapath = '../dataset/day.csv'  # 数据文件路径

cb = pd.read_csv(dapath)  # 以csv格式读取数据

# print "cb　data type is %s" % cb.dtypes  # 输出各字段数据类型

# print cb.head()  # 打印文件头部内容，查看各字段前五列数据值

# print cb.info()  # 查看数据基本信息，数据规模行列数，对应数据类型、是否有空值，存储量；

# print cb.describe()  # 描述各字段属性

# sns.distplot(cb, bins=30, kde=False) # 数据中有str，不能直接使用，需要先处理；

#  sns.distplot(cb.cnt.values, bins=30, kde=False) # 画出总租车人数的直方图；

# 总租车人数点状分布
# plt.scatter(range(cb.shape[0]), cb['cnt'].values, color='purple')
# plt.title(u"总租车人数分布")
# 使用seaborn　ditplot() 方法时，怎么忽略数据中的非数值？
# TODO 怎么使用jupyter;
# TODO CB数据探索；






