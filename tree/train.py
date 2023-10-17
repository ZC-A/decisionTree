from collections import Counter
import logging
from config import conf


header = conf.get('header')

# def train(train_data, ):


def find_best_split(train_data, feature_ids):
    try:
        n = len(feature_ids) - 1
        length = len(train_data)
        labels = [train_data[i][-1] for i in range(len(train_data))]  # 获取标签
        gini_splits = []
        attr_values = []
        gini_feature = []

        for i in range(n):
            att_vals = [train_data[j][feature_ids[i]] for j in range(len(train_data))]  # 获得当前特征 每个训练样本的值
            att_count = Counter(att_vals)  # 使用 Counter 统计

            # 计算每一个特征值的基尼系数
            for attribute in att_count.keys():
                att_subset = [[att_vals[i], labels[i]] for i in range(len(att_vals)) if att_vals[i] == attribute]  # 找出和当前特征值相同的子集
                other_subset = [[att_vals[i], labels[i]] for i in range(len(att_vals)) if att_vals[i] != attribute]  # 找出和当前特征值不同的子集
                labels_of_subset = [att_subset[i][1] for i in range(len(att_subset))]  # 获得特征值相同子集的标签
                labels_of_others = [other_subset[i][1] for i in range(len(other_subset))]  # 获得特征值不同的子集的标签
                attr_len = len(att_subset)
                subsets_count = Counter(labels_of_subset)  # 统计标签数量 Y/N
                gini = (1 - sum((v / attr_len)**2 for v in subsets_count.values())) * attr_len / length  # 只有两种标签 等价计算出 1 - (p_x**2 + p_y**2)
                others_count = Counter(labels_of_others)  # 同理
                gini += (1 - sum((v / (length - attr_len))**2 for v in others_count.values())) * (length - attr_len) / length
                gini_splits.append(gini)
                attr_values.append(attribute)
                gini_feature.append(feature_ids[i])

        gini_v = min(gini_splits)
        ind = gini_splits.index(gini_v)
        feature_id = gini_feature[ind]
        attr_value = attr_values[ind]

        best_split_att = header[feature_id]
        best_split_attr = attr_value

        logging.info('best split attr: {}, attr value: {}, Gini value: {}'.format(best_split_att, best_split_attr, str(min(gini_splits))))

        return best_split_att, best_split_attr
    except Exception as e:
        logging.error(str(e))
        logging.error('calculate error')


# def build_tree():
