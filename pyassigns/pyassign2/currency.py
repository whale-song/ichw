#!/usr/bin/env python3

'''currency.py: 通过向特定服务器请求以进行货币兑换。

__author__ = 'Whale Song'
__pkuid__ = '1800011751'
__email__ = 'whalesong@pku.edu.cn'
__version__ = '1.2.2'
'''
# v1.0
# 完成了程序总框架搭建。

# v1.1
# 添加了测试模块和随机输入模块。
# 改善了输入/输出的视觉效果。
# 增加了输入合法性判断，优化了部分算法。

# v1.2.1
# 重新编写了test函数，将期望值分组并分别进行测试。
# 移除了BYR货币，以修复服务器不支持的问题。

# 调用url模块和随机模块
from urllib.request import urlopen
import random

# 部分参数初始化
global currency_from, currency_to, amount_from
currency_list = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
                 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
                 'BSD', 'BTC', 'BTN', 'BWP', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP',
                 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP',
                 'DZD', 'EEK', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL',
                 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 
                 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 
                 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 
                 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 
                 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MTL', 'MUR', 
                 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 
                 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 
                 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 
                 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 
                 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 
                 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 
                 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL'] # 货币列表，输入合法性检测用。

test_list = [['usd', 'eur', '2.5', '2.1589225 Euros'], 
             ['czk', 'yqd', '138', '7410.6638720284 Iraqi Dinar'], 
             ['zwl', 'npr', '657', '231.79486268324 Nepalese Rupees'], 
             ['sll', 'kyd', '663', '0.065885210131108 Cayman Islands Dollars'], 
             ['sos', 'btn', '267', '32.789035515231 Bhutanese Ngultrum']]

line = '-'*30

# 数据输入函数
def data_input():
    '''输入三个变量currency_from、currency_to和amount_from
       currency_from: 源货币种类
       currency_to: 输出货币种类
       amount_from: 兑换量'''
    global currency_from, currency_to, amount_from
    currency_from = input('请输入源货币种类:').upper()
    currency_to = input('请输入要转换的货币种类:').upper()
    amount_from = input('请输入兑换量:')

# 货币兑换主函数
def exchange():
    '''兑换功能主体函数，通过获取三个输入变量编写相应url请求，从请求获取相应数据后返回amount_to
       amount_to: 输出货币量（带单位）
       url_request: 指向目标服务器的url请求内容
       doc: 请求的网页变量
       docstr: 获取的字节流
       jstr: 解码后的json格式字符串
       strdict: eval后获得的字典'''
    global amount_to
    url_request = str('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' 
        + currency_from.upper() + '&to=' + currency_to.upper() + '&amt=' + amount_from) # url请求
    doc = urlopen(url_request)                          # 从网页抓取数据
    docstr = doc.read()
    doc.close()
    jstr = (docstr.decode('ascii')).replace('true', 'True')
    jstr = jstr.replace('false', 'False')
    strdict = eval(jstr)
    if strdict['success'] == True:
        amount_to = strdict['to']
        return amount_to
    else:
        return '出现错误，错误原因：' + strdict['error']

# 输入合法性检测函数
def test_input():
    '''输入合法性检测函数，判断手动输入的三个变量是否合法（是否在规定的货币列表内，兑换量是否为合法数字）
       testnum: 获取兑换量变量amount_from的浮点数表示'''
    if  currency_from in currency_list and currency_to in currency_list:
        try:
            testnum = float(amount_from)
        except ValueError:
            return '输入有误，请确保兑换量为数字。'
        else:
            return '输入合法。'
    elif (currency_from in currency_list) == False:
        return '输入有误，源货币种类不合法。'
    elif (currency_to in currency_list) == False:
        return '输入有误，输出货币种类不合法。'

# 输出检测函数
def test_output():
    '''预设期望值，通过assert检测exchange()是否与期望值相同。'''
    global currency_from, currency_to, amount_from      # 声明全局变量
    for test_element in test_list:                      # 调取预设数据
        currency_from = test_element[0]
        currency_to = test_element[1]
        amount_from = test_element[2]
        try:
            assert exchange() == test_element[3]
        except AssertionError:
            return 'exchange()模块存在问题，程序中止。'    # 当任何一项检测出现问题时，终止程序并报告错误信息。
            break
        else:
            return '测试无误，程序可正常运行。'            # 当一项检测合格时，报告正常。

# 随机输入模块（检测用）
def random_input(p):
    global currency_from, currency_to, amount_from
    currency_from = currency_list[random.randint(0,170)]
    currency_to = currency_list[random.randint(0,170)]
    amount_from = str(random.randrange(1000))
    if p == True:
        print(
            line + '\n' + '本次随机结果：\n'
            + '输入货币：' + currency_from + '\n'
            + '输出货币：' + currency_to + '\n'
            + '兑换量：' + amount_from
        )

def main():
    print('运行检测中...')
    print(test_output())
    while test_output() == '测试无误，程序可正常运行。':   # 无限循环，使查询函数可不限次使用。
        rj = input('是否采取随机输入？ y/n \n')
        if rj == 'n':
            data_input()                                # 数据输入函数
        elif rj == 'y':
            random_input(True)                          # 随机输入函数
        else:
            print('输入不合法，请检查您的输入：是(y)/否(n)')
            main()
        if test_input() != '输入合法。':                  # 输入合法性测试函数
            print(test_input())                         # 若输入不合法，输出不合法变量类型。
            break                                       # 输出不合法时终止循环
        exchange()                                      # 执行兑换主函数
        print(line + '\n转换结果：\n' +  exchange() + '\n' + line)

if __name__ == '__main__':
    main()

    
