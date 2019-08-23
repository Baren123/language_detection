#coding: utf-8

import os
import re


class GetCountryLanguage(object):

    def getLanguageratio(self, input_text):
        # input_str = re.sub("[\s+\.\!\/_,()%^*$`(+\"\']+|[+——！，。？、~@#￥%……&*{}【】=（）]+", "",input_text)
        input_str = re.sub("[_\W]+", "",input_text)
        print(input_str)
        zh = en = ja = ko = other = 0
        for ch in input_str:
            if ch >= u'\u4e00' and ch <=u'\u9fa5':
                zh = zh + 1
            elif (ch >= u'\u0041' and ch <= u'\u005a') or (ch >= u'\u0061' and ch <= u'\u007a'):
                en = en + 1
            elif ch >= u'\u3040' and ch <= u'\u31ff':
                ja = ja + 1
            elif (ch >= u'\u3130' and ch <= u'\u318F') or (ch >= u'\uAC00' and ch <= u'\uD7A3'):
                ko = ko + 1
            else:
                other = other + 1
        print("China:{},English:{},Jap:{},Ko:{},other:{}".format(zh,en,ja,ko,other))
        total = zh + en + ja + ko + other
        dirct = {'zh':zh/total,'en':en/total,'ja':ja/total,'ko':ko/total,'other':other/total}
        return dirct


if __name__ == '__main__':
    language_radio_dirct = {}
    # check_str = "/*& //，，，$！！！【】!!@@@@@——！，。？、~@#￥%……&*{}【】=（）@@￥%（（（（))))hello,wor_ ...   ld,世界, こんにちは,중국123สวัสดีค่ะ"
    check_str = "/*& //，，，$！！！【】!!@@@@@——！，在几米的世界里，向左走，向右ああ いつのか かがこのを走，爱与错过，一步之遥。？、~@#나는 바보처럼 멍하니 서있네요￥%……&*{}【】=（）@@￥%（hello,world!（（（))))123สวัสดีค่ะ"
    language_conunty = GetCountryLanguage()
    language_radio_dirct = language_conunty.getLanguageratio(check_str)
    print(language_radio_dirct)








