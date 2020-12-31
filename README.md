# Genetic-algorithm-fits-images
Use genetic algorithm to fit images.
推荐初始参数：
triangle_number = 200#三角形数目
population = 4#种群数量
Variation_posibility=60#变异几率

用法：
将figure.png改为要拟合的图像，size改为该图像尺寸即可开始运行。运行过程中程序会自动存档，若要接之前的种群继续运行请在开始时按照提示输入按1。

文件结构：
image-保存中间步骤生成的图片
data.npy-种群数据
stable：
¬chromosome-比较完善的种群数据
¬picture-比较完善的图片
previous-曾经使用的算法
