x = int(input())

def year(x):
	if x >= 1800 and ((x % 4 == 0 and x % 100 != 0) or x % 400 == 0):
		print(1)
	elif x < 1800:
		return 0
	else:
		print(0)

if __name__ == '__main__':
	year(x)
