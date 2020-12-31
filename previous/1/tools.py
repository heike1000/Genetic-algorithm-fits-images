from matplotlib import pyplot as plt
import numpy as np
import re
import random

#pip install --index-url https://pypi.tuna.tsinghua.edu.cn/simple XXX

def generate_pic(gene_pic_raw,name):#根据个体基因矩阵生成对应图像
    ax = plt.subplot()
    plt.axis('off')
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    for i in range(100):
        gene_input = [np.hstack((gene_pic_raw[i, :][0:3], gene_pic_raw[i, :][0])),  #x坐标
                      np.hstack((gene_pic_raw[i, :][3:6], gene_pic_raw[i, :][3])),  #y坐标
                      gene_pic_raw[i, :][-1] * 0.01,  #透明度
                      (gene_pic_raw[i, :][-2] * 0.01, gene_pic_raw[i, :][-3] * 0.01, gene_pic_raw[i, :][-4] * 0.01)]#颜色
        ax.fill(gene_input[0],gene_input[1],alpha=gene_input[2],color=gene_input[3])
    plt.savefig(('gene_pic/%s.png')%name)
    plt.close('all')



def translate(data,to):#个体基因矩阵与二进制字符串的互相转化
    #将个体的基因矩阵转化为二进制字符串
    if to == "binary":
        gene_pic_binary = data.flatten()#二进制版的基因，将数组拉直
        result = ""#储存最后的二进制结果，7000位
        for i in range(len(gene_pic_binary)):
            gene_pic_binary_new = bin(gene_pic_binary[i]).replace("0b","")
            while len(gene_pic_binary_new)<7:#在二进制前面补0
                gene_pic_binary_new = "0" + gene_pic_binary_new
            result = result + gene_pic_binary_new
        return result

    #将二进制字符串转化为个体的基因矩阵
    if to == "martrix":
        gene_cut = re.findall('.......',data)
        gene_cut = [int(i,2) for i in gene_cut]
        for i in range(len(gene_cut)):
            if gene_cut[i]>100:
                gene_cut[i] = 100
        gene_cut = np.array(gene_cut).reshape(100,10)
        return gene_cut

def hybridization(gene1,gene2,variation_rate):
    #生成1个屏蔽模板
    model1 = []
    for i in range(7000):
        model1.append(random.randint(0, 1))
    #开始杂交
    new_gene1 = ""
    for i in range(7000):
        #屏蔽模板为1则使用gene1，为0则使用gene2。1/variation_rate的几率发生变异。
        if model1[i] == 1:
            if random.randint(1,variation_rate) == 1:
                new_gene1 = new_gene1 + gene2[i]
            else:
                new_gene1 = new_gene1 + gene1[i]
        if model1[i] == 0:
            if random.randint(1, variation_rate) == 1:
                new_gene1 = new_gene1 + gene1[i]
            else:
                new_gene1 = new_gene1 + gene2[i]

    return new_gene1

def fitness(tar,fig):
    #逐像素计算图形相似度,越大越好
    distance = 1 - (np.sum(np.abs(tar - fig)) / 235008000)
    return distance

if __name__ == '__main__':
    gene_pic_raw = np.random.randint(0, 100, (100, 10))
    # 0~100随机数，150个三角形，每个三角形10个参数。
    # 这是个体基因矩阵，大小为100*10。每个个体由100个三角形组成。

