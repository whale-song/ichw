# lab5 第二题
alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
alphabet2 = alphabet1.upper()
code1 = 'nopqrstuvwxyzabcdefghijklm'
code2 = code1.upper()

x = input()
tab1 = x.maketrans(alphabet1,code1)
tab2 = x.maketrans(alphabet2,code2)
x = x.translate(tab1)
x = x.translate(tab2)
print(x)
input()
