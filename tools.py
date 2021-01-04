import function


# 将一个个体变成指定大小的种群
def Reproduction(name, after, size, polygon_number):  # name指向的应该是一个个体染色体的npy数据
    origin = function.Operate(None, 'read', name)
    new = []
    for i in range(after):
        new.append(function.Variation(origin, polygon_number, 'hard', 100, size))
    function.Operate(new, 'write', 'reproduction.npy')


def Optimize(name, epoch, degree, size, polygon_number):
    pass


if __name__ == '__main__':
    Reproduction('best.npy', 20, (350, 441), 4)
