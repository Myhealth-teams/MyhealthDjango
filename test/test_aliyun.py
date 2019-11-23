#!/usr/bin/python3
# coding: utf-8

import requests


def get_backcard(kard_no):
    appcode = '8da62386451b48039ee360c05295cf6c'  # AppCode

    url = 'http://bankaera.market.alicloudapi.com/bankcard'
    headers = {
        'Authorization': 'APPCODE ' + appcode
    }

    params = {
        'kahao': kard_no,
    }
    resp = requests.get(url, params, headers=headers)
    if resp.status_code == 200:
        print('--请求成功---')
        resp_data = resp.json()
        return resp_data

    else:
        print('请求失败!')


def valid_backcard(card_no, idcard, real_name):
    url = 'http://yhkr.market.alicloudapi.com/communication/personal/1886'

    data = {
        'acct_no': card_no,
        'idcard': idcard,
        'name': real_name
    }

    appcode = '你自己的AppCode'  # 必须企业级实名认证


def valid_nidcard(real_name, idcard):
    url = 'https://naidcard.market.alicloudapi.com/nidCard'
    params = {
        'idCard': idcard,
        'name': real_name
    }

    headers = {
        'Authorization': 'APPCODE 8da62386451b48039ee360c05295cf6c'
    }

    resp = requests.get(url, params, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    else:
        return "请求失败!"


# print(get_backcard('6222020200077642839'))
print(valid_nidcard('狄玉环', '342423198410065257'))
