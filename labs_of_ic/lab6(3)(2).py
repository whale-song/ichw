a = eval(input())
b = eval(input())
l1 = a*len(b)*2
l2 = b*len(a)
c = False

for i in range(len(l1)-len(l2)):
	d = l1[slice(i, i+len(l2))]
	if d == l2:
		c = True
print(c)
