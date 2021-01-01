import numpy as np
import random
import tools
import gc
from scipy import misc
import multiprocessing
import time
if __name__ == '__main__':
    # 初始化
    triangle_number = 200#三角形数目
    size = (341, 351)#图片大小,与figure一致
    population = 4#种群数量
    Variation_posibility = 60
    target = np.array(misc.imread(r"figure.png",
                                  mode="RGB"),
                      dtype=float)#目标图片
    # 读取或重写初始种群
    populations = []
    mode1 = int(input("1读取，0覆写。\n"))
    print("CPU核心数：" + str(multiprocessing.cpu_count()))
    mode2 = int(input("输入1使用多进程加速，种群数量巨大且CPU核心较多时可选。种群数量大时请关掉电脑上所有无关软件。\n"))
    if mode1 == 1:
        populations = tools.Operate(None, 'read')
    elif mode1 == 0:
        for i in range(population):
            populations.append(tools.Generate_chromosome(triangle_number,size))
    else:
        raise Exception
    #主循环
    for a in range(100000000):
        head = time.time()
        # 生成图像
        if mode2 == 1:
            Pool = multiprocessing.Pool()
            for b in range(population):
                Pool.apply_async(tools.Generate_image,args=(populations[b], str(b),size))
            Pool.close()
            Pool.join()
        else:
            for b in range(population):
                tools.Generate_image(populations[b], str(b),size)
        # 计算图像适应度
        populations_fitnesses = []
        for c in range(population):
            populations_fitnesses.append(
                tools.Fitness(target,
                              np.array(misc.imread(r"image/%s.png" % (c),
                                                   mode="RGB"),
                                       dtype=float),size))
        print("图形相似度最大值/平均值/最小值：" + str(max(populations_fitnesses) * 100) + "%，" +
              str((sum(populations_fitnesses) / len(populations_fitnesses)) * 100) + "%，" +
              str(min(populations_fitnesses) * 100) + "%。")
        # 选取前50%，保存最佳
        rank = sorted(list(zip(populations_fitnesses, populations)))[::-1]
        tools.Generate_image(rank[0][1], "best",size)
        # 杂交，变异
        father = []
        mother = []
        father = rank[0:int(population / 2)]
        mother = rank[0:int(population / 2)]
        random.shuffle(mother)
        populations = []
        for d in range(int(population / 2)):
            populations.append(tools.Variation(tools.Hybridization(father[d][1],
                                                                   mother[d][1]),
                                               triangle_number,
                                               'soft', Variation_posibility ,size))  # 百分之x几率变异
            populations.append(tools.Variation(tools.Hybridization(father[d][1],
                                                                   mother[d][1]),
                                               triangle_number,
                                               'medium', Variation_posibility ,size))  # 百分之x几率变异
        # 每20轮备份一次
        if a % 20 == 0:
            print("已备份。")
            tools.Operate(populations, 'write')
        print("每轮耗时：" + str(time.time()-head))
        gc.collect()