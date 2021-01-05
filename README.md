# Genetic-algorithm-fits-images
Use genetic algorithm to fit images.  
推荐初始参数：  
polygon_number = 100#多边形数目。该值越大拟合能力越强，运算速度越慢。  
size = (X, X)#图片大小,与figure.png一致  
population = 6#种群数量。该值越大拟合能力越强，运算速度越慢。  
Variation_posibility = 100#变异几率。该值越大搜索能力越强，相似度上升越慢。  
policy = 'mean'#初始化策略。  
degree = 'hard'#变异强度。hard：一次改变polygon的所有参数，medium：一次改变一个polygon的一个参数，soft：一次以较小范围改变一个polygon的一个参数。  
force = 0  # 强制进化选项。前期建议设为0，相似度较高时改为1。  

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
