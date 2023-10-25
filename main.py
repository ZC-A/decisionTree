import sys
from load.load import load_data, write_tree, load_tree
import logging
from tree.evaluate import evaluate
from tree.structure import  print_tree
from tree.train import train
from config import conf



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s : line %(lineno)s %(funcName)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    train_data, eva_data = load_data()
    while True:
        input_char = input('Please enter operations: \n T for training new tree and save; \n E for using current tree to evaluate (which will be error if no tree load or train before);\n Q for quit \n')
        if input_char == 'Q':
            logging.info('Exiting..')
            exit(0)
        elif input_char == 'T':
            root = train(train_data, conf.get('feature_ids'))
            with open("output.txt", "w",encoding="utf-8") as f:
                # 保存原来的标准输出
                original_stdout = sys.stdout
                # 重定向标准输出到文件
                sys.stdout = f
                # 在这里执行需要输出的代码
                print_tree(root)
                # 还原标准输出
                sys.stdout = original_stdout
            write_tree(root)
            logging.info('save tree sucess')
        elif input_char == 'E':
            root = load_tree()
            if not root:
                logging.error('no tree available')
                continue
            eva_correct_num = evaluate(eva_data, root, conf.get('feature_ids'))
            logging.info('evaluation correct nums: ' + str(eva_correct_num))
            logging.info('evaluation correct rates: ' + str(eva_correct_num / len(eva_data)))
