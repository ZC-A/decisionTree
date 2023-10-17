
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
        
def evaluate(eva_data, tree_node,feature_ids):
    length = len(eva_data)
    sum=0
    for i in range(length):
        data = eva_data[i]
        sum+=test(data, tree_node,feature_ids)
    return sum