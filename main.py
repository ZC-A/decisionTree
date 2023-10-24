from collections import deque
from typing import List
from load.load import load_data
import logging
from tree.structure import node
from tree.evaluate import evaluate
from tree.train import train
from config import conf


def levelOrder(root: [node]) -> List[List[int]]:
    list1 = []
    q = deque()
    q.append(root)
    while q:
        level = []
        for i in range(len(q)):
            poping = q.popleft()
            if poping:
                level.append(poping.feature_value)
                q.append(poping.left)
                q.append(poping.right)
        if level:
            list1.append(level)
    return list1


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s : line %(lineno)s %(funcName)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    train_data, eva_data = load_data()
    root = train(train_data, conf.get('feature_ids'))
    # eva_correct_num = evaluate(eva_data, root, conf.get('feature_ids'))
    # logging.info('evaluation correct nums: ' + str(eva_correct_num))
    # logging.info('evaluation correct rates: ' + str(eva_correct_num / len(eva_data)))
