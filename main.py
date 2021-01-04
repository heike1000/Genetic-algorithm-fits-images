import numpy as np
import random
import function
import gc
from scipy import misc
import multiprocessing
import time

# pip install --index-url https://pypi.tuna.tsinghua.edu.cn/simple XXX
start = time.time()
if __name__ == '__main__':
    # 初始化
    polygon_number = 200  # 多边形数目。该值越大拟合能力越强，运算速度越慢。
    size = (300, 400)  # 图片大小,与figure.png一致
    population = 6  # 种群数量。该值越大拟合能力越强，运算速度越慢。
    Variation_posibility = 100  # 变异几率。该值越大搜索能力越强，相似度上升越慢。
    policy = 'random'  # 初始化策略
    degree = 'medium'  # 变异强度。hard：一次改变polygon的所有参数，medium：一次改变一个polygon的一个参数，soft：一次以较小范围改变一个polygon的一个参数。
    force = 0  # 强制进化选项。
    target = np.array(misc.imread(r"cache/figure.png",
                                  mode="RGB"),
                      dtype=float)  # 目标图片
    # 读取或重写初始种群
    populations = []
    mode1 = int(input("输入1读取data.npy，输入0覆写data.npy。\n"))
    mode2 = int(input("输入1使用多进程模式。(可能使每轮耗时减少。)\n"))
    if mode1 == 1:
        populations = function.Operate(None, 'read', 'cache/chromosome/data.npy')
    elif mode1 == 0:
        for i in range(population):
            populations.append(function.Generate_chromosome(polygon_number, size, policy))
    else:
        raise Exception
    # 主循环
    for a in range(100000000):
        head = time.time()
        # 生成图像
        if mode2 == 1:
            Pool = multiprocessing.Pool()
            for b in range(population):
                Pool.apply_async(function.Generate_image, args=(populations[b], str(b), size))
            Pool.close()
            Pool.join()
        else:
            for b in range(population):
                function.Generate_image(populations[b], str(b), size)
        # 计算图像适应度
        populations_fitnesses = []
        for c in range(population):
            populations_fitnesses.append(
                function.Fitness(target,
                                 np.array(misc.imread(r"cache/image/%s.png" % (c),
                                                      mode="RGB"),
                                          dtype=float), size))
        print("图形相似度最大值/平均值/最小值：" + str(max(populations_fitnesses) * 100) + "%，" +
              str((sum(populations_fitnesses) / len(populations_fitnesses)) * 100) + "%，" +
              str(min(populations_fitnesses) * 100) + "%。")
        # 选取前50%，保存最佳
        rank = sorted(list(zip(populations_fitnesses, populations)))[::-1]
        function.Generate_image(rank[0][1], "best", size)
        # 杂交，变异
        father = []
        mother = []
        father = rank[0:int(population / 2)]
        mother = rank[0:int(population / 2)]
        random.shuffle(mother)
        populations = []
        if force == 1:
            # 最优秀个体直接进入下一轮，并将变异一次的自身也放入下一轮
            populations.append(father[0][1])
            populations.append(
                function.Variation(function.Hybridization(father[0][1], mother[0][1]), polygon_number, degree,
                                   Variation_posibility, size))
            for d in range(int(population / 2) - 1):
                for e in range(2):
                    populations.append(
                        function.Variation(function.Hybridization(father[d + 1][1],mother[d + 1][1]), polygon_number,degree,
                                    Variation_posibility, size))  # 百分之x几率变异
        elif force == 0:
            for d in range(int(population / 2)):
                for e in range(2):
                    populations.append(function.Variation(function.Hybridization(father[d][1],
                                                                                 mother[d][1]), polygon_number, degree,
                                                          Variation_posibility, size))  # 百分之x几率变异
        # 每20轮备份一次
        if a % 20 == 0:
            print("已备份。")
            function.Operate(populations, 'write', 'cache/chromosome/data.npy')
            function.Operate(rank[0][1], 'write', 'cache/chromosome/best.npy')
        print("每轮耗时：" + str(time.time() - head) + "s，总共耗时：" + str((time.time() - start) / 3600) + "h")
        gc.collect()
