l1 = eval(input())
l2 = eval(input())
if len(l1) >= len(l2):
	l2 *= int(len(l1)/len(l2))
else:
	l1 *= int(len(l2)/len(l1))

def judge():
	for i in range(len(l2)):
		if l2[i] == l1[0]:
			if (l2[i:] + l2[:i]) == l1:
				return True

if judge() == True:
	print(True)
else:
	print(False)