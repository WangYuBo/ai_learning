# 菜鸟如何在ubuntu16.04中安装opencv?
opencv是一个跨平台的计算机视觉库.以BSD许可证授权发行，可以在商业和研究领域中免费使用。OpenCV可用于开发实时的图像处理、计算机视觉以及模式识别程序.学习计算视觉方面经常用到.


先看流程:
> 
1. 安装anaconda;为什么安装它?现在不同python版本都在使用,它能让不同版本python干净/整洁的共处.这样安装:[ubuntu16安装conda2](https://blog.csdn.net/woainishifu/article/details/74978647)
2. 在conda中创建python3虚拟环境:
3.[howto  conda install opencv ](https://blog.csdn.net/wds2435629591/article/details/78694463)
4. 验证: conda 下 python进入python3环境,之后import cv2 ,然后 cv2.__version__,显示版本号,表示安装成功.


你肯定会问:为什么不直接用python3安装呢? ;
conda 是 Anaconda 下用于包管理和环境管理的命令行工具，是 pip 和 vitualenv 的组合。安装成功后 conda 会默认加入到环境变量中，因此可直接在命令行窗口运行 
如果你熟悉 virtualenv，那么上手 conda 非常容易，不熟悉 virtulenv 的也没关系，它提供的命令就几个，非常简单。我们可以利用 conda 的虚拟环境管理功能在 Python2 和 Python3 之间自由切换.
