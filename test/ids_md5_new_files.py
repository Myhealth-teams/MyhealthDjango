#!/usr/bin/python3
# coding: utf-8

import hashlib
import string
import random
import time
import uuid


def compute_time(f):
    def wrapper(*args):
        start_time = time.time()
        ret = f(*args)
        timedelta = time.time() - start_time
        print(timedelta)

        return ret
    return wrapper


def new_id(len):
    c_ = []
    for i in range(len):
        c_.append(random.choice(string.digits+string.ascii_letters))

    return ''.join(c_).lower()


@compute_time
def gen_ids(size=100):
    with open('ids.txt', 'w') as f:
        ids = [new_id(10)+("" if _ == size-1 else "\n") for _ in range(size)]

        f.writelines(ids)
        print(len(set(ids)))


def new_md5(str=None):
    if str:
        return hashlib.md5(str.encode()).hexdigest()
    return hashlib.md5(uuid.uuid4().hex.encode()).hexdigest()


@compute_time
def gen_md5(size=500000):
    with open('ids.txt', 'r') as f:
        ids = f.readlines()

    with open('md5s.txt', 'w') as mf:
        print(len(ids))
        for _ in range(size):
            flag = random.random()
            if flag > 0.5 and ids:
                id = ids.pop(0 if len(ids) <= 1 else random.randint(0, len(ids)-1))
                mf.write(new_md5(id)+"\t"+(random.choice(['baidu', 'toutiao', 'tencent']) if flag > 0.8 else ""))
            else:
                mf.write(new_md5()+"\t"+(random.choice(['baidu', 'toutiao', 'tencent']) if flag < 0.3 else ""))

            if _ != size -1 :
                mf.write("\n")



if __name__ == '__main__':
    gen_ids(10000)
    gen_md5()