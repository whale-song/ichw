#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "WhaleSong"
__pkuid__  = "1800011751"
__email__  = "whalesong@pku.edu.cn"
"""

# python wcount.py http://www.gutenberg.org/cache/epub/19033/pg19033.txt 20

import sys
from urllib.request import urlopen, URLError

replace_list = [',', '.', '?', '!', '\"', '\"', '[', ']', '_', ';', '/', '-', '\'s', '(', ')']

def check_request():
    '''check if the input url and lines exist and legal.
    '''
    import os
    # 用os库ping google服务器以检测网络连接

    try:
        sys.argv[1]
    except IndexError:      # 检测网址正确性
        print('输入格式不正确，请输入网址。')
        return False

    if os.system('ping 8.8.8.8'):
        print('ping fall. internet disconnected.')
        return False
    else:
        try:
            urlopen(sys.argv[1])    # 测试打开网页
        except (URLError, ValueError) as e:
            print('404 Error')
            return False
        else:
            return True

def requesting_data():
    '''read the lines in the page given. return the data collected from the page.
    '''
    homepage = urlopen(sys.argv[1])
    docs = homepage.readlines()     # 全部读取
    homepage.close()
    return docs

def update_dictionary(line, dictionary):
    '''read the word in a line then update the dictionary collecting the words counted.
    '''
    line = line.lower()     # 变为小写
    for i in replace_list:
        line = line.replace(i, ' ')     # 替换所有标点
    words = line.split()    # 拆分为单词
    for word in words:
        if word in dictionary.keys():
            dictionary[word] += 1   # 若已有键则计数
        else:
            dictionary.update({word:1})     # 若无键则增加条目

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    words_count = dict()    # 创建用于计数的字典
    for aline in lines:
        aline = aline.decode('utf-8')
        update_dictionary(aline, words_count)   # 调用更新字典函数
    sorted_dict = sorted(
        words_count.items(),
        key=lambda x : x[1],
        reverse=True)       # 对字典元素进行排序
    return sorted_dict[:int(topn)]

def main():
    '''main function to run the functions above.
    '''
    if check_request() == True:
        print('检测通过。')
        for i in wcount(requesting_data(), sys.argv[2] if len(sys.argv)==3 else 10):
            print(i)

if __name__ == '__main__':
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        input()
        sys.exit(1)
    else:
        main()