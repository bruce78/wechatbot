#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import requests
import itchat
import re

headers = {"Accept-Language": "zh-CN,en;q=0.5"}


def match(text):
    keys = pattern_dict.keys()
    for key in keys:

        obj = re.match(key, text, re.M | re.I)
        if obj:
            return pattern_dict[key]

    return


pattern_dict = {}


def get_coins():
    url = 'https://www.bitlook.com/public/web/api/v1/cap/market/list'
    try:
        r = requests.get(url, headers=headers).json()
        result_list = r.get('result')

        for x in result_list:
            key = r'(\w*\s)*' + x + '(\w*\s)*'
            pattern_dict[key] = x

        return result_list
    except:
        return


coin_names = get_coins()


def get_coin(name):
    url = 'https://www.bitlook.com/public/web/api/v1/cap/market/'+name+'/USD'
    try:
        r = requests.get(url, headers=headers).json()
        return r.get('result')
    except:
        return


def get_view_point(coin):
    url = 'https://www.bitlook.com/public/web/api/v1/viewpoint/related/coin/'+coin
    try:
        r = requests.get(url, headers=headers).json()
        return r.get('result')
    except:
        return


def response(text):
    coin = match(text)
    if coin:
        obj = get_coin(coin)
        if obj is None:
            return

        array0 = []
        array0.append(coin + "行情快报 - \n")
        array0.append("https://www.bitlook.com/#/market/base/" + coin + "\n")
        array0.append("现价：$" + obj['price'] + "\n")
        array0.append("24小时涨跌幅：" + obj['percentage'] + "%\n")
        array0.append("24小时成交额：$" + str(obj['volume']) + "\n")
        if text.find('look') != -1 or text.find('LOOK') != -1:
            articles = get_view_point(coin)
            if len(articles) != 0:
                array0.append("\n" + coin + "相关资讯:\n")
                for article in articles:
                    article_id = article['articleId']
                    array0.append(article['authorName'] + ": " + article['title']+" \n")
                    array0.append("https://www.bitlook.com/#/article/viewpoint/" + str(article_id)+" \n")

                    if article['summary'] is not None:
                        array0.append("摘要: ")
                        array0.append(article['summary'])
                        array0.append("\n")

        return ''.join(map(str, array0))

    return


# , isGroupChat=True
@itchat.msg_register(itchat.content.TEXT, isFriendChat=False, isGroupChat=True)
def coin_reply(msg):

    reply = response(msg['Text'])
    return reply


itchat.auto_login(hotReload=True, picDir="bb.jpg")
itchat.run()


# print(response('look ETC'))
