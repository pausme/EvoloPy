import random
import numpy as np
import time
import math
from solution import solution


def DBO(obgj, lb, ub, dim, PopSize, iters):
    P_percent = 0.2
    pNum = round(P_percent * PopSize)

    s = solution()
    # 检查 lb和ub 是否为列表类型 如果不是，则转之是
    if not isinstance(lb, list):
        lb = [lb] * dim
    if not isinstance(ub, list):
        ub = [ub] * dim

    # 初始化
    X = np.zeros([PopSize, dim])
    for i in range(PopSize):
        for j in range(dim):
            X[i, j] = np.random.rand() * (ub[j] - lb[j]) + lb[j]
    
    # 得到种群适应度值
    pop = X.shape[0]
    fitness = np.zeros([pop, 1])
    for i in range(pop):
        fitness[i] = obgj(X[i, :])

    # 得到种群适应度值的下标
    Fit = np.sort(fitness, axis=0)
    Fit_index = np.argsort(fitness, axis=0)

    # 根据适应度来进行排序
    X_new = np.zeros(X.shape)
    for i in range(pop):
        X_new[i, :] = X[Fit_index[i], :]

# 接下来就是种群的四大行为更新
    