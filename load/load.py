import logging
import csv
from config import conf
import pickle


def load_data():
    try:
        logging.info('Using header: ' + str(conf.get('header', [])))
        logging.info('loading data and remove missing values and native-country: ...')  # 移除指定列和含有缺失值的列
        train_data, eva_data = [], []
        with open(conf.get('trainingPath'), 'r', encoding='utf-8') as f:
            for row in csv.reader(f, delimiter=','):
                row = [r.strip() for r in row]
                if '?' in row or not row:
                    continue
                # r = []
                # for ids in feature_ids:
                    # r.append(row[ids])
                train_data.append(row)
        logging.info('load train data complete')
        with open(conf.get('evaluationPath'), 'r', encoding='utf-8') as f:
            for row in csv.reader(f, delimiter=','):
                row = [r.strip() for r in row]
                if '?' in row or not row:
                    continue
                # r = []
                # for ids in feature_ids:
                # r.append(row[ids])
                eva_data.append(row)
        logging.info('load eva data complete')
        logging.info('training data has: ' + str(len(train_data)))   # 训练集和测试集
        logging.info('evaluation data has: ' + str(len(eva_data)))
        return train_data, eva_data
    except Exception as e:
        logging.error(str(e))
        logging.error('loading fail')


def load_tree():
    try:
        with open('tree.pickle', 'rb') as f:  # 二进制读写决策树
            tree = pickle.load(f)
            return tree
    except Exception as e:
        logging.error(str(e))
        logging.error('loading decision tree failed')
        return None


def write_tree(tree):
    try:
        with open('tree.pickle', 'wb') as f:
            pickle.dump(tree, f)
    except Exception as e:
        logging.error(str(e))
        logging.error('write decision tree failed')
