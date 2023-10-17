import copy
from collections import Counter
import logging
from config import conf

from tree.structure import node



header = conf.get('header')


def train(train_data, feature_ids):
    if not train_data:
        return None
    labels = [train_data[i][-1] for i in range(len(train_data))]
    labels_count = Counter(labels)

    same_attr = True
    for feature_id in feature_ids:
        attr = [train_data[i][feature_id] for i in range(len(train_data))]
        attr_count = Counter(attr)
        if len(attr_count) != 1:
            same_attr = False
            break

    tree_node = node()  # 检查两个条件 1.是否标签唯一  2.所有属性相同或剩余训练数据长度小于某个特定值

    if len(labels_count) == 1:
        tree_node.isleaf = True
        tree_node.label = list(labels_count.keys())[0]   # 返回唯一标签值
        return tree_node
    elif len(feature_ids) == 1 or same_attr or len(train_data) < 100:  # 返回剩余数据中标签的众数
        tree_node.isleaf = True
        tree_node.label = max(labels_count.keys(), key=labels_count.get)
        return tree_node

    best_split_att, best_split_attr, attr_data, other_data = find_best_split(train_data, feature_ids)
    tree_node = node()
    tree_node.feature_id = header.index(best_split_att)
    tree_node.feature_value = best_split_attr
    feature_ids_copy = copy.deepcopy(feature_ids)
    feature_ids_copy.remove(header.index(best_split_att))
    # print(feature_id)
    dummy = node()
    dummy.isleaf = True
    dummy.label = max(labels_count.keys(), key=labels_count.get)
    l, r = train(attr_data, feature_ids_copy), train(other_data, feature_ids)
    tree_node.left = l if l else dummy
    tree_node.right = r if r else dummy
    return tree_node


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

        #logging.info('best split attr: {}, attr value: {}, Gini value: {}'.format(best_split_att, best_split_attr, str(min(gini_splits))))

        attr_data, other_data = [train_data[i] for i in range(length) if train_data[i][feature_id] == attr_value], [train_data[i] for i in range(length) if train_data[i][feature_id] != attr_value]

        # best_split_att 最佳分割属性
        # best_split_attr 最佳分割属性值
        # attr_data 左叶子节点
        # other_data 右子树
        return best_split_att, best_split_attr, attr_data, other_data
    except Exception as e:
        logging.error(str(e))
        logging.error('calculate error')



def test(data, tree_node,feature_ids):
        n = len(feature_ids) - 1
        length = len(data)
        att_vals = data[tree_node.feature_id]  # 获得当前特征
        label = data[-1].strip('.')  # 获取标签
        num=0
        if tree_node.isleaf:
            if tree_node.label==label:
                return 1
            else:
                return 0
        if att_vals==tree_node.feature_value :
                num=test(data, tree_node.left,feature_ids)
        else:
                num=test(data, tree_node.right,feature_ids)
        return num
        
def recursive(eva_data, tree_node,feature_ids):
    length = len(eva_data)
    sum=0
    for i in range(length):
        data = eva_data[i]
        sum+=test(data, tree_node,feature_ids)
    return sum