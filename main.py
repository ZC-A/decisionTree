from load.load import load_data
import logging
from tree.train import find_best_split
from tree.train import init_tree
from tree.train import train
from config import conf


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s : line %(lineno)s %(funcName)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    train_data, eva_data = load_data()
    tree_root=init_tree(train_data)
    res0=train(train_data, conf.get('feature_ids'),tree_root)
    #res = find_best_split(train_data, conf.get('feature_ids'))
