# coding=utf-8

from twilio.rest import Client
from datetime import datetime
import time

account_sid = 'AC4918bc12e1d27d6c50d2497de6068aa'
auth_token = '103250f358bf446789e71501f17a977'
def sendsms(things):
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            from_='+180625210',
            body=things,
            to='+8613002537')
        return True
    except Exception as e:
        return False

    #print(message.sid)

getthings = {'8':"breakfast time", '12':"lunch time", '18':'dinner time', '22':"goodnight"}


if __name__ == "__main__":
    while True:
        now = datetime.now()
        for hour in getthings.keys():
            if now.hour == int(hour):
                thing = getthings.get(hour, 'What are you doing')
                send = sendsms(thing)
                if send:
                    time.sleep(60*60)#如果发送成功，就暂停一小时，免得重复发送
                else:
                    print('send SMS failed!')
