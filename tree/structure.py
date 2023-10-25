from config import conf
from collections import deque
from typing import Optional
class node():
    def __init__(self) -> None:
        self.feature_id = -1
        self.feature_value = None
        self.feature_type = None
        self.left = None
        self.right = None
        self.label = None
        self.isleaf = False
    

header = conf.get('header')


def print_tree(current_node:node, nameattr='feature_value', left_child='left', right_child='right', indent='', last='updown'):

    if hasattr(current_node, nameattr) is not None:
        name = lambda node: getattr(node, nameattr)

    up = current_node.left
    down = current_node.right

    if up is not None:
        next_last = 'up'
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '|', ' ' * len(str("["+header[current_node.feature_id]+":"+str(current_node.feature_value)+"]")))
        print_tree(up, nameattr, left_child, right_child, next_indent, next_last)

    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'

    if up is not None and down is not None: end_shape = '┤'
    elif up: end_shape = '┘'
    elif down: end_shape = '┐'
    else: end_shape = ''

    if current_node.feature_value is None:
        print('{0}{1}{2}{3}'.format(indent, start_shape, "["+current_node.label+"]", end_shape))
    else:
        print('{0}{1}{2}{3}'.format(indent, start_shape, "["+header[current_node.feature_id]+","+str(current_node.feature_value)+"]", end_shape))

    if down is not None:
        next_last = 'down'
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '|', ' ' * len(str("["+header[current_node.feature_id]+":"+str(current_node.feature_value)+"]")))
        print_tree(down, nameattr, left_child, right_child, next_indent, next_last)
