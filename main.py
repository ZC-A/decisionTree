from load.load import load_data
import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s : line %(lineno)s %(funcName)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    train_data, eva_data = load_data()
