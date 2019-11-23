<<<<<<< HEAD

import requests

HOST = '122.112.231.109'
PORT = 9200

INDEX = 'yloa'

def create_index(index_name='yloa'):
=======
#!/usr/bin/python3
# coding: utf-8

import requests

HOST = '119.3.170.97'
PORT = 80  # 默认的是 9200

INDEX = 'jyoa'


def create_index(index_name='jyoa'):
>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22
    global INDEX
    INDEX = index_name
    url = f'http://{HOST}:{PORT}/{index_name}'
    json = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        }
    }

    # 调用增加索引的接口
    resp = requests.put(url, json=json)
    print(resp.json())


def remove_index():
    url = f'http://{HOST}:{PORT}/{INDEX}'
    resp = requests.delete(url)
    ret = resp.json()
    print(ret)


def add_doc(doc: dict, doc_type: str):
    # dict 对象中不存在id的key时会抛出异常吗？ 会
    doc_id = doc.pop('id') if 'id' in doc.keys() else None

    url = f'http://{HOST}:{PORT}/{INDEX}/{doc_type}' \
          + ("/"+str(doc_id) if doc_id else '')

    resp = requests.post(url, json=doc)
    ret = resp.json()
    if ret.get('result') == 'created':
        print('添加doc成功')
        return True

    print(ret)
    print('添加doc失败')
    return False


def remove_doc(doc_type, doc_id):
    url = f'http://{HOST}:{PORT}/{INDEX}/{doc_type}/{doc_id}'
    resp = requests.delete(url)
    ret = resp.json()
    if ret.get('result') == 'deleted':
        print('删除成功')
        return True

    print('删除失败')
    return False


def search(keyword):
<<<<<<< HEAD
    url = f'http://{HOST}:{PORT}/_all/_search?q={keyword}'
=======
    url = url = f'http://{HOST}:{PORT}/_all/_search?q={keyword}'
>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22
    resp = requests.get(url)
    ret = resp.json()
    hits = ret.get('hits').get('hits')
    if hits:
        datas = []
        for source in hits:
            source_ = source.get('_source')
            source_['id'] = source.get('_id')

            datas.append(source_)

        return datas # 返回搜索后的数据


if __name__ == '__main__':

    # doc = {
    #     'id': 1,
    #     'name': 'disen',
    #     'sex': '男',
    #     'age': 20
    # }
    # create_index()
<<<<<<< HEAD
    add_doc(doc, 'person')
    # remove_doc('person1', 'w5_3lW4BMRCZTBbTXLkQ')
    # remove_index()

    print(search(''))
=======
    # add_doc(doc, 'person')
    # remove_doc('person1', 'w5_3lW4BMRCZTBbTXLkQ')
    # remove_index()

    print(search('少儿'))


>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22
