#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from qqbot import QQBot

class MyQQBot(QQBot):
    def onPollComplete(self, msgType, from_uin, buddy_uin, message):
        if message == '-hello':
            self.send(msgType, from_uin, '你好，我是QQ机器人')
        elif message == '-stop':
            self.stopped = True
            self.send(msgType, from_uin, 'QQ机器人已关闭')

try:
	bot = MyQQBot()
	bot.LoginAndRun()
except KeyboardInterrupt:
        sys.exit(0)
