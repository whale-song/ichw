# lab5 第一题
bd = ['!', '?', ',', '.', ';']
x = str(input())
j = 0

for i in bd:
	x = x.replace(i, ' ')

def count(x):
	global j
	strlist = x.split()
	for a in strlist:
		antiword = ''
		for b in range(len(a)):
			antiword = antiword + a[-1-b]
		if a == antiword:
			j+=1



if __name__ == '__main__':
	count(x)
	print(j)
	input()
