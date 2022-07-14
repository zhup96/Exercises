# coding: utf-8
# Team : FMS Tester
# Author：Zhup
# Date ：2022/7/13 19:54

# 练习二十六：提取网页中的手机号码

import re


def get_web_phone_number():
    pattern = r"1[3-9]\d{9}"
    with open('./practice_file/web_phone_number') as fn:
        file_cont = fn.read()
    result = re.findall(pattern, file_cont)
    print(result)


# 练习二十七：列表A去重，将去重元素对应B列表的元素相加
def compute_number(lista, listb):
    cache = {}
    for index, number in enumerate(lista):
        if number not in cache:
            cache[number] = {"sum": listb[index], "count": 1}
        cache[number]["sum"] += listb[index]
        cache[number]["count"] += 1
    print(cache)


# 练习二十八：提取字符串中的邮箱

def get_str_email():
    word = """电子邮箱格式： fvxfvv@126.com
                fvxfvv@163.com
                fvxfvv@qq.com ；
                这些就是电子邮箱额格式；希望能够帮助你！"""
    pattern = re.compile(
        r"""
        [a-zA-Z0-9_-]+
        @
        [a-zA-Z0-9]+
        \.
        [a-zA-Z]{2,4}
        """,
        re.VERBOSE
    )

    results = pattern.findall(word)

    for result in results:
        print(result)


"""练习二十九：验证用户密码是否正确。要求：1、长度大于8位小于10位
2、必须包含一个大写英文字母
3、必须包含一个小写英文字母
4、必须包含一个数字
5、必须包含一个特殊字符"""


def check_password(pwd):
    if not 8 <= len(pwd) <= 10:
        return False, "msg:密码长度必须在8~10位"
    if not re.findall(r"[a-z]", pwd):
        return False, "msg:密码必须包含小写英文字母"
    if not re.findall(r"[A-Z]", pwd):
        return False, "msg:密码必须包含大写英文字母"
    if not re.findall(r"[0-9]", pwd):
        return False, "msg:密码必须包含数字"
    if not re.findall(r"[^0-9a-zA-Z]", pwd):
        return False, "msg:密码必须包含1个特殊字符"
    return True, "msg:密码可用"


"""#练习三十：利用正则表达式提取商品信息
例如：小明买了1斤黄瓜，花了7块钱
      2斤白糖，花了10块钱
      1斤桃子，花了5块钱
提取内容：（1，黄瓜，7）
"""


def get_goods_price():
    info = """
      小明买了1斤黄瓜，花了7块钱
      2斤白糖，花了10块钱
      1斤桃子，花了5.8块钱
    """
    for line in info.split("\n"):
        pattern = r"(\d)斤(.*)花了(\d+(\.\d+)?)块钱"
        match = re.search(pattern, line)
        if match:
            print(f'{match.group(1)}\t{match.group(2)}\t{match.group(3)}')


"""#练习三十一：利用正则表达式对文章中的电话号码进行加密
例如：锄禾13408445765日当午17809397543
     123汗滴禾下土1115298675434
加密内容：13*********
"""


def encrypt_phone():
    info = """
    锄禾13408445765日当午17809397543
     123汗滴禾下土1115298675434
    """
    pattern = r"(1[3-9])\d{9}"
    print(re.sub(pattern, r"\1#########", info))


# 练习三十二：格式化多种时间格式，统一按照：YYYY-MM-DD输出

def format_data():
    info = """
    锄禾2022/07/14日当午2022.07.15
     07-16-2022汗滴禾下土7/17/2022
    """
    info = re.sub(r"(\d{4})/(\d{2})/(\d{2})", r"\1-\2-\3", info)
    info = re.sub(r"(\d{4})\.(\d{2})\.(\d{2})", r"\1-\2-\3", info)
    info = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\1-\2", info)
    info = re.sub(r"(\d{1})/(\d{2})/(\d{4})", r"\3-\1-\2", info)
    print(info)


# 练习三十三： 利用正则表达式对英文文章进行分词，统计词频
import pandas as pd


def split_file_get_word():
    with open('./practice_file/word') as fn:
        info = fn.read()
    words = re.split(r"[\s.()\"-?]+", info)
    print(pd.Series(words).value_counts()[:10])


# 练习三十四：对中文文章进行分词
import jieba


def split_chinese_word():
    info = """他是无意穿堂风，却偏偏孤据引山洪。我是垂眉摆渡翁，却独独偏爱哝。
　　忽然想起那年夏日毕业之际，我送他的藏头巧妙情诗，还有在QQ的匿名坦白说，还有我第一次鼓起勇气隐晦的告白，
   毕业后我想着也许在我们笑着说再见时候深知再见遥遥无期，我想过叫他一起来学习预习新课，如今想想对我而言珍贵如斯"""
    info = re.sub(r"[\s。，\n]+", "", info)
    word_list = jieba.cut(info)
    # print(list(word_list))
    print(pd.Series(word_list).value_counts()[:10])


# 练习三十五：以递归的方式倒叙打印输入的字符串

def output(s, l):
    len(s)
    if l == 0:
        return
    print(s[l - 1])
    output(s, l - 1)

#练习三十六：第一个人为10岁，后面的人依次比第一个大两岁。利用递归法返回岁数

def age(n):
    if n == 1:
        c = 10
    else:
        c = age(n - 1) + 2
    return c


if __name__ == "__main__":
    # lista = [1, 1, 2, 2, 3, 3, 1, 4]
    # listb = [3, 4, 5, 6, 7, 7, 6, 8]
    # compute_number(lista, listb)
    # get_web_phone_number()
    # get_str_email()
    # print("12345Aa#",check_password("12345Aa#"))
    # print("12345Aa23", check_password("12345Aa23"))
    # print("12345A23#", check_password("12345A23#"))
    # get_goods_price()
    # encrypt_phone()
    # format_data()
    # split_file_get_word()
    # split_chinese_word()

    s = input('Input a string:')
    l = len(s)
    output(s, l)
    # print(age(3))