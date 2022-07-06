# coding: utf-8
# Team : FMS Tester
# Author：Zhup
# Date ：2022/7/5 22:08

# 练习一:返回给定数字前的平方和

def square_sum(number):
    result = 0
    while number > 0:
        result += number * number
        number -= 1
    print(result)


import math


# 练习二：给定圆半径，计算圆面积

def compute_area_of_circle(r):
    return round(math.pi * r * r, 2)


if __name__ == '__main__':
    # square_sum(number=10)
    print(compute_area_of_circle(r=2))
