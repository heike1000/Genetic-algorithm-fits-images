import function
import numpy as np
from scipy import misc


# 将一个个体变成指定大小的种群
def Reproduction(name, after, size, polygon_number):  # name指向的应该是一个个体染色体的npy数据
    origin = function.Operate(None, 'read', name)
    new = []
    for i in range(after):
        new.append(function.Variation(origin, polygon_number, 'hard', 100, size ,1))
    function.Operate(new, 'write', 'data.npy')


def Optimize(name, epoch, degree, size, polygon_number, chance, Variation_number):
    origin = function.Operate(None, 'read', name)
    function.Generate_image(origin, 'origin', size)
    target = np.array(misc.imread(r"cache/figure.png", mode="RGB"), dtype=float)  # 目标图片
    for i in range(epoch):
        origin_score = function.Fitness(target, np.array(misc.imread(r"origin.png", mode="RGB"), dtype=float), size)
        competitor = function.Variation(origin, polygon_number, degree, chance, size, Variation_number, 1)
        function.Generate_image(competitor, 'competitor', size)
        competitor_score = function.Fitness(target, np.array(misc.imread(r"competitor.png", mode="RGB"), dtype=float),
                                            size)
        if competitor_score > origin_score:
            origin = competitor
            function.Generate_image(origin, 'origin', size)
        print(origin_score)


if __name__ == '__main__':
    Reproduction('best.npy', 16, (300, 400), 4)
