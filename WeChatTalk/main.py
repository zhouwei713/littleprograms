# coding=utf-8

from wxpy import *
import requests
from threading import Timer

def get_content():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content_e = r.json()['content']
    content_c = r.json()['note']
    return content_e, content_c

bot = Bot(cache_path = True)
def send_chat():
    try:
        content_e, content_c = get_content()
        #此处填微信名称，可不是微信号哦
        dear_friend = bot.friends().search(u'你的心上人')[0]
        dear_friend.send(content_e)
        dear_friend.send(content_c)
        t = Timer(86400, send_chat) #86400秒就是一天啦
        t.start()
    except Exception as e:
        print('send fail!')




if __name__ == '__main__':
    send_chat()