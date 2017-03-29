#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
from qqbot import QQBot
from qqbot.qqbotcls import QQMessage
from qqbot.messagefactory import Message

from langwiki.langwiki_resources import LangwikiResources

class MyQQBot(QQBot):
    mMyName = u"@机器人小薇"
    mVersion = "0.02"
    mLangwikiRes = LangwikiResources()

    def GeneralReply(self, msg):
        message = msg.content.decode("utf-8").lower()
        if u"版本" in message or u"ver" in message:
            msg.Reply("么么哒，我的版本是" + self.mVersion)
            return True
        elif u"叫什么" in message or u"name" in message or u"名字" in message:
            msg.Reply("我叫小薇，您忠实的小秘书 [笑]")
            return True
        elif u"hello" in message or u"你好" in message or u"hi" in message:
            msg.Reply("你好！小薇愿意为主人服务～")
            return True
        elif u"男朋友" in message or u"boyfriend" in message or u"气质" in message or u"少女" in message:
            msg.Reply("人家害羞嘛～ 有机会私聊好吗？")
            return True
        elif u"漂亮" in message or u"美丽" in message:
            msg.Reply("是吗？你眼光真好哦 ^_^")
            return True
        return False

    def GroupAtMe(self, msg):
        message = msg.content.decode("utf-8")
        message = message.replace(self.mMyName, "").strip()
        processed = False
        if len(message) == 1:
            # dictionary call
            msg.Reply(self.mLangwikiRes.lookupHanzi(message).encode("utf-8"))
            return

        smsg = message.encode("utf-8")
        if smsg.startswith("manchu")# or smsg.startswith("滿") or smsg.startswith("满"):
            if smsg.startswith("manchu"):
                smsg = smsg[6:].strip()
            if smsg.startswith("滿") or smsg.startswith("满"):
                smsg = smsg[1:].strip()
            mandef = self.mLangwikiRes.lookupManchu(smsg)
            if mandef != None:
                msg.Reply(mandef.encode("utf-8"))
                return
            else:
                msg.Reply("抱歉，小薇没找到任何结果～")
                return

        if not self.GeneralReply(msg):
            msg.Reply("小薇还看不懂，请以后再试 [笑]")

    def Process(self, msg):
        if (type(msg) is QQMessage):
            message = msg.content.decode("utf-8")
            if self.mMyName in message:
                return self.GroupAtMe(msg)
            elif message == '!!stop':
                self.Stop(code=0)
                msg.Reply('么么哒，886')

        super(QQBot, self).Process(msg)

try:
  bot = MyQQBot()
  bot.LoginAndRun()
except KeyboardInterrupt:
  sys.exit(0)
