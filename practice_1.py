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


# 练习三:给定数字范围区间，输出所有素数

def is_prime(number):
    if number in (1, 2):
        return True
    for ind in range(2, number):
        if number % ind == 0:
            return False
    return True


def print_prime(begin, end):
    for number in range(begin, end + 1):
        if is_prime(number):
            print(number)


# 练习四：给定数字N，求前N个数字的平方和

def sum_of_square(number):
    result = 0
    while number > 0:
        result += number * number
        number -= 1
    print(result)


# 练习五：计算两个数字列表的和
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listb = [3, 5, 7, 9]


def sum_list(a, b):
    print(sum(a + b))


# 练习五：给出数字区间，利用列表推导式输出偶数
begin = 10
end = 20
data = [item for item in range(begin, end + 1) if item % 2 == 0]

# 练习七：从列表a中移除列表b元素
listc = [item for item in lista if item not in listb]


# 练习八：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def random_four_number():
    for one in range(1, 5):
        for two in range(1, 5):
            for three in range(1, 5):
                if (one != two) and (one != three) and (two != three):
                    print(f'{one}{two}{three}')


# 练习九：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，
# 可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
def compute_bonus():
    profit = int(input('净利润:'))
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    bonus = 0
    for idx in range(0, 6):
        if profit > arr[idx]:
            bonus += (profit - arr[idx]) * rat[idx]
            profit = arr[idx]
    print(bonus)


# 练习十：打印指定个数的斐波那契数列
def feb(num):
    if num == 1:
        return [1]
    if num == 2:
        return [1, 1]
    fe = [1, 1]
    for i in range(2, num):
        fe.append(fe[-1] + fe[-2])
    return fe


# 练习十一：输出九九乘法表
def haskell():
    for i in range(1, 10):
        print()
        for j in range(1, i + 1):
            print(f'{i}*{j}={i * j}', end=' ')


# 练习十二：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def compute_height():
    degree = int(input("请输入弹跳次数："))
    height = 100
    result = 0
    for num in range(1, degree + 1):
        result += height + height / 2
        height = height / 2
    return result, height


# 练习十三：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个。
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。
# 到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
def compute_peach():
    num = 1
    for day in range(9, 0, -1):
        x1 = (num + 1) * 2
        num = x1
    print(num)


# 练习十四：统计文件中中英文单词出现的次数

def compute_word():
    word_count = {}
    file_path = './practice_file/word'
    with open(file_path, 'r') as fn:
        for lines in fn:
            line = lines[:-1]
            words = line.split()
            for word in words:
                if word not in word_count:
                    word_count[word] = 0
                word_count[word] += 1
    return word_count


# 练习十五：统计指定目录下文件打小
import os


def compute_size():
    file_size = {}
    for file in os.listdir('.'):
        if os.path.isfile(file):
            file_size[file] = f'{os.path.getsize(file) / 1000}kb'
    return file_size


# 练习十六：按照文件的不同后缀汇总整理文件
import shutil


def file_tidying():
    path = './arrange_file'
    for file in os.listdir(path):
        ext = os.path.splitext(file)[1]
        ext = ext[1:]
        if not os.path.isdir(f'{path}/{ext}'):
            os.mkdir(f'{path}/{ext}')

        source_path = f'{path}/{file}'
        target_path = f'{path}/{ext}/{file}'
        # 移动文件
        shutil.move(source_path, target_path)


# 练习十七：计算文件中学生的分数，并计算出最大值、最小值、平均值

def compute_student_score():
    score_info = {}
    with open('./practice_file/student_info') as fn:
        for lines in fn:
            line = lines[:-1]
            course, name, score = line.split(',')
            if course not in score_info:
                score_info[course] = []
            score_info[course].append(int(score))
    for course,score in score_info.items():
        print(
            course,
            max(score),
            min(score),
            sum(score)/len(score)
        )


if __name__ == '__main__':
    # square_sum(number=10)  #练习一
    # print(compute_area_of_circle(r=2))   #练习二
    # print_prime(begin=10, end=20)      #练习三
    # sum_of_square(number=3)
    # sum_list(lista, listb)
    # print(data)
    # print(listc)
    # random_four_number()
    # compute_bonus()
    # print(feb(10))
    # haskell()
    # print(compute_height())
    # compute_peach()
    # print(sorted(compute_word().items(), reverse=True, key=lambda x: x[1])[:10])
    # print(compute_size())
    # file_tidying()
    compute_student_score()