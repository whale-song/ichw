# 作者：宋怀雨
# 化学与分子工程学院

# 货币兑换v1.0
# 完成了程序总框架搭建。

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

# 数据输入函数
def data_input():
	global currency_from, currency_to, amount_from
	currency_from = input('请输入源货币种类:').upper()
	currency_to = input('请输入要转换的货币种类:').upper()
	amount_from = input('请输入源货币量:')

# 货币兑换主函数
def exchange():
	url_request = str('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' 
		+ currency_from.upper() + '&to=' + currency_to.upper() + '&amt=' + amount_from) # url请求
	doc = urlopen(url_request) # 从网页抓取数据
	docstr = doc.read()
	doc.close()
	jstr = docstr.decode('ascii')
	jstr = jstr.replace('true', 'True')
	strdict = eval(jstr)
	amount_to = strdict['to']
	return amount_to

def test_input():
	if  currency_from in currency_list and currency_to in currency_list and type(amount_from) == float:
		return '输入合法。'
	elif (currency_from in currency_list) == False:
		return '输入有误，源货币种类不合法。'
	elif (currency_to in currency_list) == False:
		return '输入有误，输出货币种类不合法。'
	elif amount_from.isdigit() == False:
		return '输入有误，请检查源货币量。'

def test_exchange():
	pass

if __name__ == '__main__':
	while True:
		data_input()
		if test_input() != '输入合法。':
			print(test_input())
			break
		exchange()
		print('转换结果为:\n' + exchange())
	

