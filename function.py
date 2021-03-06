import copy
import numpy as np
import random
import warnings
from PIL import Image, ImageDraw

warnings.filterwarnings('ignore')


# 生成染色体
def Generate_chromosome(plygon_number, size, method):
    # R G B ALPHA X0 Y0 X1 Y1 X2 Y2 X3 Y3(当前使用四边形)
    chromosome = []
    if method == 'random':
        for a in range(plygon_number):
            DNA = []
            for b in range(4):
                DNA.append(random.randint(0, 255))
            for c in range(4):
                DNA.append(random.randint(0, size[0]))
                DNA.append(random.randint(0, size[1]))
            chromosome.append(DNA)
        return chromosome
    elif method == 'mean':
        for a in range(plygon_number):
            DNA = []
            for b in range(4):
                DNA.append(0)
            for c in range(4):
                DNA.append(0)
                DNA.append(0)
            chromosome.append(DNA)
        return chromosome


# 根据染色体生成照片
def Generate_image(chromosome, name, size):
    img = Image.new('RGBA', size=size)
    draw_img = ImageDraw.Draw(img)
    draw_img.polygon([(0, 0), (0, size[1]), (size[0], size[1]), (size[0], 0)], fill=(255, 255, 255, 255))
    for i in range(len(chromosome)):
        img_polygon = Image.new('RGBA', size=size)
        draw_polygon = ImageDraw.Draw(img_polygon)
        draw_polygon.polygon([(chromosome[i][4], chromosome[i][5]),
                              (chromosome[i][6], chromosome[i][7]),
                              (chromosome[i][8], chromosome[i][9]),
                              (chromosome[i][10], chromosome[i][11])],
                             fill=(chromosome[i][0],
                                   chromosome[i][1],
                                   chromosome[i][2],
                                   chromosome[i][3]))
        img = Image.alpha_composite(img, img_polygon)
    img.save(r'cache/image/%s.png' % name)
    img.close()


# 变异
def Variation(chromosome, polygon_number, degree, chance, size, times):
    if random.randint(0, 100) <= chance:
        if degree == "hard":
            for i in range(times):
                DNA = []
                for b in range(4):
                    DNA.append(random.randint(0, 255))
                for c in range(4):
                    DNA.append(random.randint(0, size[0]))
                    DNA.append(random.randint(0, size[1]))
                new = copy.deepcopy(chromosome)
                new[random.randint(0, polygon_number - 1)] = DNA
        elif degree == 'medium':
            new = copy.deepcopy(chromosome)
            for i in range(times):
                pick = random.randint(0, 8)
                if pick == 0 or pick == 1 or pick == 2 or pick == 3:
                    new[random.randint(0, polygon_number - 1)][pick] = random.randint(0, 255)
                elif pick == 4 or pick == 6 or pick == 8 or 10:
                    new[random.randint(0, polygon_number - 1)][pick] = random.randint(0, size[0])
                else:
                    new[random.randint(0, polygon_number - 1)][pick] = random.randint(0, size[1])
        elif degree == 'soft':
            new = copy.deepcopy(chromosome)
            for i in range(times):
                pick = random.randint(0, 11)
                if pick == 0 or pick == 1 or pick == 2 or pick == 3:
                    new[random.randint(0, polygon_number - 1)][pick] += random.randint(0, 25)
                    if new[random.randint(0, polygon_number - 1)][pick] > 255:
                        new[random.randint(0, polygon_number - 1)][pick] = 255
                    elif new[random.randint(0, polygon_number - 1)][pick] < 0:
                        new[random.randint(0, polygon_number - 1)][pick] = 0
                elif pick == 4 or pick == 6 or pick == 8 or 10:
                    new[random.randint(0, polygon_number - 1)][pick] += int(random.randint(0, size[0]) * 0.1)
                    if new[random.randint(0, polygon_number - 1)][pick] > size[0]:
                        new[random.randint(0, polygon_number - 1)][pick] = size[0]
                    elif new[random.randint(0, polygon_number - 1)][pick] < 0:
                        new[random.randint(0, polygon_number - 1)][pick] = 0
                else:
                    new[random.randint(0, polygon_number - 1)][pick] += int(random.randint(0, size[1]) * 0.1)
                    if new[random.randint(0, polygon_number - 1)][pick] > size[1]:
                        new[random.randint(0, polygon_number - 1)][pick] = size[1]
                    elif new[random.randint(0, polygon_number - 1)][pick] < 0:
                        new[random.randint(0, polygon_number - 1)][pick] = 0
        return new
    else:
        return chromosome


# 适应度计算
def Fitness(target, image, size):
    distance = 1 - (np.sum(np.abs(target - image)) / (255 * size[0] * size[1] * 3))
    return distance


# 文件读，写
def Operate(data, method, name):
    if method == 'read':
        raw = np.load(name)
        return raw.tolist()
    elif method == 'write':
        writefile = np.array(data)
        np.save(name, writefile)


# 杂交
def Hybridization(chromosome1, chromosome2):
    model = []
    chromosome_new = []
    for a in range(len(chromosome1)):
        model.append(random.randint(0, 1))
    for b in range(len(chromosome1)):
        if model[b] == 0:
            chromosome_new.append(chromosome1[b])
        elif model[b] == 1:
            chromosome_new.append(chromosome2[b])
    return chromosome_new


if __name__ == '__main__':
    pass
