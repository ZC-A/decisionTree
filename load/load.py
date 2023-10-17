import logging
import csv
from config import conf


def load_data():
    try:
        logging.info('Using header: ' + str(conf.get('header', [])))
        logging.info('loading data and remove missing values and native-country: ...')
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
        logging.info('training data has: ' + str(len(train_data)))
        logging.info('evaluation data has: ' + str(len(eva_data)))
        return train_data, eva_data
    except Exception as e:
        logging.error(str(e))
        logging.error('loading fail')
