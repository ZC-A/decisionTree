from collections import Counter
import logging

# def train(train_data):


def find_best_split(train_data, feature_ids):
    n = len(feature_ids) - 1
    d = len(train_data)
    labels = [train_data[i][-1] for i in range(len(train_data))]  # 获取标签
    gini_splits = []

    for i in range(n):
        att_vals = [train_data[j][i] for j in range(len(train_data))]  # 获得每个特征的值
        att_count = Counter(att_vals)  # 使用 Counter 统计
        gini_vals = []
        nr_subsets = []

        # 计算每一个特征值的基尼系数
        for attribute in att_count.keys():
            att_subset = [[att_vals[i], labels[i]] for i in range(len(att_vals)) if att_vals[i] == attribute]  # 找出和当前特征值相同的子集
            nr = len(att_subset)  # 子集长度
            nr_subsets.append(nr)
            labels_of_subset = [att_subset[i][1] for i in range(len(att_subset))]  # 获得子集的标签
            local_c = Counter(labels_of_subset)
            gini = 1 - sum((v / nr)**2 for v in local_c.values())  # 只有两种标签 等价计算出 1 - (p_x**2 + p_y**2)
            gini_vals.append(gini)

        gs = sum((nr_subsets[x] / d) * gini_vals[x] for x in range(len(nr_subsets)))
        gini_splits.append(gs)

    logging.info('best split: {} Gini value: {}'.format(str(gini_splits.index(min(gini_splits))), str(min(gini_splits))))

    return gini_splits.index(min(gini_splits))
