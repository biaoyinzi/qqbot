#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
import random, time, sys, subprocess
import requests
import json

class LangwikiResources:
    def __init__(self):
        return

    def lookupHanzi(self, hanzi):
        url = 'http://langwiki.org/tools/dict/php/query.php'
        #url = 'http://localhost/php/query.php'
        settings = [
            "0", # pu
            "4", # ct
            "0", # kr
            "0", # vn
            "0", # jp
            "0", # ltco
            "1", # ltcp
            "0", # match
            "0", # mn
            "0"  # wu
        ]

        # Set POST fields here
        post_fields = {
			"string": hanzi,
			"mode": "0",
			"flag[]": [
                "0", # only
                "0", # variants
                "1"  # annotation
            ],
			"setting[]": settings,
            "bot": "1"
        }

        r = requests.post(url, data = post_fields)
        if r.status_code != 200:
            return hanzi + u" 請讓小薇好好想想這個問題。。。（服务器快点啊）"

        res = json.loads(r.text)
        if "HTML" in res:
            answer = u"太好了，主人，小薇給您找到了答案～ "
            answer += res["HTML"]
        else:
            answer = u"嗚嗚，這個字小薇暫時想不起來了～ 請稍後再問我吧"
        return answer

    def lookupWord(self, word):
        return "err: not implemened"
