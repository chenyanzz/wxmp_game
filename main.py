# -*- coding: utf-8 -*-  

import werobot
import game
import conf
import tools

robot = werobot.WeRoBot()
tools.robot = robot

'''
msg:
    ToUserName:
    FromUserName:
    CreateTime:
    Content:
    MsgId:
'''
@robot.text
def reply(msg, session):
    return game.onUserReply(msg, session)

# 让服务器监听在 127.0.0.1:80
robot.config.from_object(conf.RobotConfig)

if not conf.is_demo:
    robot.run()

