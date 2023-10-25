import copy
import csv

def test(data, tree_node, feature_ids):
    att_vals = data[tree_node.feature_id]  # 获得当前特征
    label = data[-1].strip('.')  # 获取标签
    num = 0
    if tree_node.isleaf:
        if tree_node.label == label:
            return 1
        else:
            return 0
    if tree_node.feature_type == 'Integer':
        if int(att_vals) <= tree_node.feature_value:
            num = test(data, tree_node.left, feature_ids)
        else:
            num = test(data, tree_node.right, feature_ids)
        return num
    else:
        if att_vals == tree_node.feature_value:
            num = test(data, tree_node.left, feature_ids)
        else:
            num = test(data, tree_node.right, feature_ids)
        return num



def evaluate(eva_data, tree_node, feature_ids):
    length = len(eva_data)
    eva_res = copy.deepcopy(eva_data)
    num = 0
    for i in range(length):
        data = eva_data[i]
        iscorrect = test(data, tree_node, feature_ids)
        eva_res[i].append(iscorrect)
        num += iscorrect
    with open('res.csv', 'w') as f:
        writer = csv.writer(f)
        for row in eva_res:
            writer.writerow(row)
    return num
