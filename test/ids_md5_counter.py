#!/usr/bin/python3
# coding: utf-8
import time
import hashlib
from collections import Counter


def compute_time(f):
    def wrapper(*args):
        start_time = time.time()
        ret = f(*args)
        timedelta = time.time() - start_time
        print(f'{f.__name__} 函数耗时（秒）', timedelta)

        return ret

    return wrapper


def md5(id):
    return hashlib.md5(id.encode()).hexdigest()


def clear_data():
    lines = []
    with open('md5s.txt', 'r') as f:
        for line in f:
            md5_id, type_str = line.split('\t')
            if type_str != '\n':
                lines.append((md5_id, type_str[:-1]))

    return lines


@compute_time
def find_all_id():
    id_md5s = clear_data()  # 清除没有对应类型的数据
    id_md5s_dict = dict(id_md5s)  # 将剩余的数据转成字典（key: md5(id),  value: 类型）

    types = []

    with open('ids.txt', 'r') as f_:
        for id_ in f_:
            type_ = id_md5s_dict.get(md5(id_), None)
            if type_:
                types.append(type_)

    return dict(Counter(types))


if __name__ == '__main__':
    print(find_all_id())
