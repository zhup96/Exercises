# coding: utf-8
# Team : FMS Tester
# Author：Zhup
# Date ：2022/7/6 21:30
import datetime

# 计算销售额的周同比


data_sale = {}
# 文件读取去掉首行开关写法
is_first_line = True
with open('./practice_file/week_sales') as fn:
    for line in fn:
        if is_first_line:
            is_first_line = False
        else:
            line = line[:-1]
            data_s, sale = line.split("\t")
            data_sale[data_s] = float(int(sale))


def get_diff_time(data, day):
    timedelta = datetime.timedelta(days=-day)
    data_obj = datetime.datetime.strptime(data, "%Y-%m-%d")
    return (data_obj + timedelta).strftime("%Y-%m-%d")


for data, sale in data_sale.items():
    data7 = get_diff_time(data, 7)
    sale7 = data_sale.get(data7, 0)
    if sale7 == 0:
        print(data, data7, 0)
    else:
        print(data, data7, sale7,
              (sale - sale7) / sale7
              )

# if __name__ =="__main__":
