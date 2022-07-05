# coding: utf-8
# Team : FMS Tester
# Author：Zhup
# Date ：2022/7/5 22:08

# 返回给定数字前的平方和


def square_sum(number):
    result = 0
    while number > 0:
        result += number * number
        number -= 1
    print(result)


if __name__ == '__main__':
    square_sum(number=10)
