# Genetic-algorithm-fits-images
Use genetic algorithm to fit images.
推荐初始参数：
triangle_number = 200#多边形数目
population = 4#种群数量
Variation_posibility=60#变异几率

用法：
将figure.png改为要拟合的图像，size改为该图像尺寸即可开始运行。运行过程中程序会自动存档，若要接之前的种群继续运行请在开始时按照提示输入按1。

文件结构：
stable：
¬chromosome-比较完善的种群数据
¬image-比较完善的图片

cache：
¬chromosome-保存中间生成的数据
¬image-保存中间生成的图像
¬figure.png-要拟合的图像

main.py,function.py,tools.py-主程序
