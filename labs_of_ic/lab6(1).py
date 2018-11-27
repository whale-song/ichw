x = list(input().split())
a = 0
for i in x:
	if i.isdigit() == True and int(i) % 2 == 0:
		a += int(i)
print(a)