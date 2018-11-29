# 作者：宋怀雨
# 化学与分子工程学院

# 货币兑换(python源码版)

# v1.0
# 完成了程序总框架搭建。
# v1.1
# 添加了测试模块。（随机输入模块尚在建设中）
# 改善了输入/输出的视觉效果。
# 增加了输入合法性判断，优化了部分算法。

# 调用url模块
from urllib.request import urlopen

# 部分参数初始化
global currency_from, currency_to, amount_from
currency_list = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
                 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
                 'BSD', 'BTC', 'BTN', 'BWP', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 
                 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 
                 'DOP', 'DZD', 'EEK', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 
                 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 
                 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 
                 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 
                 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 
                 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MTL', 
                 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 
                 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 
                 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 
                 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 
                 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 
                 'USD', 'UYU', 'UZS', 'VEF', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 
                 'XAU', 'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL'] # 货币列表，输入合法性检测用。
line = '-'*30

# 数据输入函数
def data_input():
    global currency_from, currency_to, amount_from
    currency_from = input('请输入源货币种类:').upper()
    currency_to = input('请输入要转换的货币种类:').upper()
    amount_from = input('请输入兑换量:')

# 货币兑换主函数
def exchange():
    global amount_to
    url_request = str('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' 
        + currency_from.upper() + '&to=' + currency_to.upper() + '&amt=' + amount_from) # url请求
    doc = urlopen(url_request) # 从网页抓取数据
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = jstr.replace('true', 'True')
    jstr = jstr.replace('false', 'False')
    strdict = eval(jstr)
    amount_to = strdict['to']
    return amount_to

# 输入合法性检测函数
def test_input():
    if  currency_from in currency_list and currency_to in currency_list:
        try:
            testnum = float(amount_from)
        except(ValueError):
            return '输入有误，请确保兑换量为数字。'
        else:
            return '输入合法。'
    elif (currency_from in currency_list) == False:
        return '输入有误，源货币种类不合法。'
    elif (currency_to in currency_list) == False:
        return '输入有误，输出货币种类不合法。'

# 输出检测函数
def test_output():
    tdoc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' 
        + currency_from.upper() + '&to=' + currency_to.upper() + '&amt=' + amount_from)
    tstr = tdoc.read()
    tdoc.close()
    tstr = (tstr.decode('ascii')).replace('true', 'True')
    tstr = tstr.replace('false','False')
    tstr = eval(tstr)
    tto = tstr['to']
    if tto == amount_to:
        return '数据无误。'
    else:
        return '该数据存在问题，请联系开发者。'

# 随机输入模块（检测用）
# （建设中）
def random_input():
    import random
    global currency_from, currency_to, amount_from
    currency_from = currency_list[random.randint(0,192)]
    currency_to = currency_list[random.randint(0,192)]
    amount_from = str(random.randrange(1000))
    print(line + '\n' + '本次随机结果：\n'
        + '输入货币：' + currency_from + '\n'
        + '输出货币：' + currency_to + '\n'
        + '兑换量：' + amount_from)

def main():
    while True:     # 无限循环，使查询函数可不限次使用。
        rj = input('是否采取随机输入？ y/n \n')
        if rj == 'n':
            data_input()    # 数据输入函数
        elif rj == 'y':
            random_input()
        else:
            print('输入不合法，请检查您的输入：是(y)/否(n)')
            main()
        if test_input() != '输入合法。':     #输入合法性测试函数
            print(test_input())
            break
        exchange()
        print(line + '\n转换结果：\n' +  exchange() + '\n' + line)
        if input('是否进行测试？ y/n \n') == 'y':
            print(test_output())  
        print(line)

if __name__ == '__main__':
    main()

    
