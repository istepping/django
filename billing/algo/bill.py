import numpy as np
import pandas as pd
from . import knn


# 读文件
def read_file(file):
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'R']
    df = pd.read_csv(file, names=columns, header=None, sep="\s+")
    return df.ix[:, [0, 1, 2, 3, 4, 5]].values, df['R'].values


#############################
# @author sunLei
# @time 2018/12/8 23:39
# @note 预测器
#############################
def predict(test):
    group, label = read_file("algo/data_bill.txt")
    # 加载系数
    test = test * np.loadtxt("algo/max_right_weight.txt")
    return knn.classify_knn0(group, label, test, 1000)
