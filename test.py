# -*- coding: utf-8 -*-  
import werobot.messages

import conf
conf.is_demo = True

import main

req=""
session={}

session["phase"] = 10
session["uid"] = "cy"
session["name"] = "cy"
session["skip_times_left"] = conf.MaxSkipTimes

while True:
    req = input("用户消息：\n")
    if req=="exit":
        break
    class msg(object):
        FromUserName = "test_user_id"
        Content=req
    print("微信回复：\n%s"%main.reply(msg,session))

