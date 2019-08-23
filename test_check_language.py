#coding: utf-8

import unittest
import random
import check_language
import math

PERFOMR_SINGLE_TEST_COUNT = 5
GENERATE_ENGLISH_COUNT = 5
GENERATE_CHINESE_COUNT = 5
GENERATE_JAPAN_COUNT = 10
GENERATE_KROEAN_COUNT = 6
GENERATE_OTHER_COUNT = 10
GENERATE_SYMBOL_COUNT = 10
TOTAL_GENERATE_COUNT = GENERATE_CHINESE_COUNT + GENERATE_ENGLISH_COUNT + GENERATE_JAPAN_COUNT + GENERATE_KROEAN_COUNT + GENERATE_OTHER_COUNT

class GetCountryLanguage(unittest.TestCase):

    def getRandomWord(self, input_language_type, length):
        random_str = ''
        dirct = { 'en':'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz',
                'other':'0123456789щЮЯ',
                'symbol':'+\\.!/_,()%^*$`(+\"\']+|[+——！，。？、~@#￥%……&*{}【】=（）]+',
                'zh':'在几米的世界里向左走向右走爱与错过一步之遥',
                'ko':'나는바보처럼멍하니서있네요',
                'ja':'ああいつのかかがこのを'}
        for i in range(length):
            random_str += dirct[input_language_type][random.randint(0, len(dirct[input_language_type]) - 1)]
        return random_str


    def shuffle_str(self,s):
        str_list = list(s)
        random.shuffle(str_list)
        return ''.join(str_list)


    # def testAllEnglish(self):
    #     dir={}
    #     for i in range(PERFOMR_SINGLE_TEST_COUNT):
    #         input_str = self.shuffle_str('hello,world!')
    #         print(input_str)
    #         dir = check_language.GetCountryLanguage().getLanguageratio(self.shuffle_str(input_str))
    #         print(math.isclose(dir['en'],1.0))
    #         self.assertTrue(math.isclose(dir['en'],1.0))

    # def testAllChinest(self):
    #     dir={}
    #     for i in range(PERFOMR_SINGLE_TEST_COUNT):
    #         input_str = self.shuffle_str('在几米的世界里，向左走，向右走，爱与错过，一步之遥')
    #         print(input_str)
    #         dir = check_language.GetCountryLanguage().getLanguageratio(self.shuffle_str(input_str))
    #         self.assertTrue(math.isclose(dir['zh'],1.0))

    # def testAllJapanese(self):
    #     dir={}
    #     for i in range(PERFOMR_SINGLE_TEST_COUNT):
    #         input_str = self.shuffle_str('ああ いつのか かがこのを')
    #         print(input_str)
    #         dir = check_language.GetCountryLanguage().getLanguageratio(self.shuffle_str(input_str))
    #         self.assertTrue(math.isclose(dir['ja'],1.0))

    # def testAllKorean(self):
    #     dir={}
    #     for i in range(PERFOMR_SINGLE_TEST_COUNT):
    #         input_str = self.shuffle_str('나는 바보처럼 멍하니 서있네요')
    #         print(input_str)
    #         dir = check_language.GetCountryLanguage().getLanguageratio(self.shuffle_str(input_str))
    #         self.assertTrue(math.isclose(dir['ko'],1.0))

    # def testOther(self):
    #     dir={}
    #     for i in range(PERFOMR_SINGLE_TEST_COUNT):
    #         input_str = self.shuffle_str("/*& //，，，$！！！【】!!@@@@@——！，。？、~@#￥%……&*{}【】=（）@@￥%（（（（))))123สวัสดีค่ะ")
    #         print(input_str)
    #         dir = check_language.GetCountryLanguage().getLanguageratio(self.shuffle_str(input_str))
    #         self.assertTrue(math.isclose(dir['other'],1.0))

    # def testMixLanguage(self):
    #     dir={}
    #     for i in range(PERFOMR_SINGLE_TEST_COUNT):
    #         input_str = self.shuffle_str("/*& //，，，$！！！【】!!@@@@@——！，在几米的世界里，向左走，向右ああ いつのか かがこのを走，爱与错过，一步之遥。？、~@#나는 바보처럼 멍하니 서있네요￥%……&*{}【】=（）@@￥%（hello,world!（（（))))123สวัสดีค่ะ")
    #         print(input_str)
    #         dir = check_language.GetCountryLanguage().getLanguageratio(self.shuffle_str(input_str))
    #         print(dir)
    #         self.assertTrue(math.isclose(dir['zh'],0.328125))
    #         self.assertTrue(math.isclose(dir['en'],0.15625))
    #         self.assertTrue(math.isclose(dir['ja'],0.171875))
    #         self.assertTrue(math.isclose(dir['ko'],0.203125))
    #         self.assertTrue(math.isclose(dir['other'],0.140625))

    def testRandomMixLanguage(self):
        dir={}
        for i in range(PERFOMR_SINGLE_TEST_COUNT):
            input_str = self.getRandomWord('zh',GENERATE_CHINESE_COUNT) + self.getRandomWord('en',GENERATE_ENGLISH_COUNT) \
                        + self.getRandomWord('ja',GENERATE_JAPAN_COUNT) + self.getRandomWord('ko',GENERATE_KROEAN_COUNT) \
                        + self.getRandomWord('other',GENERATE_OTHER_COUNT) + self.getRandomWord('symbol',GENERATE_SYMBOL_COUNT)
            print(input_str)
            dir = check_language.GetCountryLanguage().getLanguageratio(self.shuffle_str(input_str))
            print(dir)
            print(GENERATE_CHINESE_COUNT/TOTAL_GENERATE_COUNT)
            self.assertTrue(math.isclose(dir['zh'],float(GENERATE_CHINESE_COUNT/TOTAL_GENERATE_COUNT)))
            self.assertTrue(math.isclose(dir['en'],float(GENERATE_ENGLISH_COUNT/TOTAL_GENERATE_COUNT)))
            self.assertTrue(math.isclose(dir['ja'],float(GENERATE_JAPAN_COUNT/TOTAL_GENERATE_COUNT)))
            self.assertTrue(math.isclose(dir['ko'],float(GENERATE_KROEAN_COUNT/TOTAL_GENERATE_COUNT)))
            self.assertTrue(math.isclose(dir['other'],float(GENERATE_OTHER_COUNT/TOTAL_GENERATE_COUNT)))



if __name__ == '__main__':
    unittest.main()
