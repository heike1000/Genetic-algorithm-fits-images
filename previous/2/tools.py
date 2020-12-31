import numpy as np
from PIL import Image, ImageDraw
import gc
import random
from scipy import misc
import warnings
import copy
import time
warnings.filterwarnings('ignore')
triangle_number = 100
size = (255,255)

def Generate_chromosome(triangle_number):#传入需要生成的三角形数目
    #R G B ALPHA X0 Y0 X1 Y1 X2 Y2
    chromosome = []
    for a in range(triangle_number):
        DNA = []
        for b in range(16):
            DNA.append(random.randint(0,255))
        chromosome.append(DNA)
    return chromosome

def Generate_image(chromosome,name):
    img = Image.new('RGBA', size=size)
    draw_img = ImageDraw.Draw(img)
    draw_img.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill=(255, 255, 255, 255))
    for i in range(len(chromosome)):
        img_triangle = Image.new('RGBA', size=size)
        draw_triangle = ImageDraw.Draw(img_triangle)
        draw_triangle.polygon([(chromosome[i][4],chromosome[i][5]),
                               (chromosome[i][6],chromosome[i][7]),
                               (chromosome[i][8],chromosome[i][9]),
                               (chromosome[i][10],chromosome[i][11]),
                               (chromosome[i][12],chromosome[i][13]),
                               (chromosome[i][14],chromosome[i][15])],
                              fill=(chromosome[i][0],
                                    chromosome[i][1] ,
                                    chromosome[i][2],
                                    chromosome[i][3]))
        img = Image.alpha_composite(img, img_triangle)
    img.save(r'image/%s.png'%name)
    img.close()

def Variation(chromosome,triangle_number,degree):
    if degree == "hard":
        DNA = []
        for b in range(16):
            DNA.append(random.randint(0, 255))
        new = copy.deepcopy(chromosome)
        new[random.randint(0, triangle_number-1)] = DNA
    elif degree == 'medium':
        new = copy.deepcopy(chromosome)
        new[random.randint(0, triangle_number - 1)][random.randint(0, 15)] = random.randint(0, 255)
    elif degree == 'soft':
        new = copy.deepcopy(chromosome)
        new[random.randint(0, triangle_number - 1)][random.randint(0, 15)] =+ random.randint(-10,10)
        if new[random.randint(0, triangle_number - 1)][random.randint(0, 15)] > 255:
            new[random.randint(0, triangle_number - 1)][random.randint(0, 15)] = 255
        elif new[random.randint(0, triangle_number - 1)][random.randint(0, 15)] < 0:
            new[random.randint(0, triangle_number - 1)][random.randint(0, 15)] = 0
    return new

def Fitness(target,image):
    distance = 1-(np.sum(np.abs(target - image))/49744125)
    return distance

def Operate(data,method):
    if method == 'read':
        raw = np.load('data.npy')
        return raw.tolist()
    elif method == 'write':
        writefile = np.array(data)
        np.save("data.npy",writefile)

if __name__ == '__main__':
    #a = Generate_chromosome(100)
    a = Operate(None,'read')
    for i in range(100000000):
        Generate_image(a, "best")
        best = Fitness(np.array(misc.imread(r"figure.png", mode="RGB"), dtype=float),
                        np.array(misc.imread(r"image/best.png", mode="RGB"), dtype=float))
        b = Variation(a,100,'soft')
        Generate_image(b, "compititor")
        compititor = Fitness(np.array(misc.imread(r"figure.png", mode="RGB"), dtype=float),
                        np.array(misc.imread(r"image/compititor.png", mode="RGB"), dtype=float))
        if compititor > best:
            a = copy.deepcopy(b)
        print("图形相似度：" + str(best*100))
        if i//500:
            Operate(a,'write')

