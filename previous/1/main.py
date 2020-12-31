import numpy as np
from scipy import misc
import random
import tools
import warnings
from tools import hybridization as hy
from tools import translate as tr
warnings.filterwarnings('ignore')

#全局初始化
target=np.array(misc.imread("figure.png",mode="RGB"),dtype=float)
number = 20
populations = []
for i in range(100):
    gene_pic_raw = np.random.randint(0, 100, (100, 10))
    populations.append(gene_pic_raw)

#主程序
while True:
    fitnesses = []
    M = []
    F1 = []
    F2 = []
    chosen = []
    #计算适应度
    for i in range(number):
        tools.generate_pic(populations[i],"gene_pic%s"%i)
        fitnesses.append(tools.fitness(target,np.array(misc.imread("gene_pic/gene_pic%s.png"%i,mode="RGB"),dtype=float)))
    max_f = 0
    max_g = 0
    for i in range(len(fitnesses)):
        if fitnesses[i]>max_f:
            max_f = fitnesses[i]
            max_g = i
    chosen.append(populations[max_g])
    print("最优：" + str(max(fitnesses)))
    print("均值：" + str(np.mean(fitnesses)))

    #选择
    fitnesses = fitnesses/sum(fitnesses)#fitnesses变成了被选择的概率
    while len(chosen)<(number/2):
        for i in range(len(fitnesses)):
            if fitnesses[i]>random.randint(0,100000000)/100000000 and len(chosen)<(number/2):
                chosen.append(populations[i])

    #杂交，变异
    M = chosen[0:5]
    F1 = chosen[5:10]
    F2 = chosen[5:10][::-1]
    populations = []

    for i in range(5):
        populations.append(tr(hy(tr(M[i], 'binary'), tr(F1[i], 'binary'), 10), 'martrix'))
        populations.append(tr(hy(tr(M[i], 'binary'), tr(F1[i], 'binary'), 10), 'martrix'))
        populations.append(tr(hy(tr(M[i], 'binary'), tr(F2[i], 'binary'), 10), 'martrix'))
        populations.append(tr(hy(tr(M[i], 'binary'), tr(F2[i], 'binary'), 10), 'martrix'))























