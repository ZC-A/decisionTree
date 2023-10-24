from load.load import load_data
import logging
from tree.evaluate import evaluate
from tree.train import train
from config import conf


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s : line %(lineno)s %(funcName)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    train_data, eva_data = load_data()
    root = train(train_data, conf.get('feature_ids'))
    eva_correct_num = evaluate(eva_data, root, conf.get('feature_ids'))
    logging.info('evaluation correct nums: ' + str(eva_correct_num))
    logging.info('evaluation correct rates: ' + str(eva_correct_num / len(eva_data)))
