s = str(input())
grade_list = []
l = list(eval(s))
for i in l:
	grade_list.append(i[1])
a = max(grade_list)
while max(grade_list) == a:
	t = len(grade_list)
	for i in range(t):
		if grade_list[i] == a:
			del grade_list[i]
			break
b = max(grade_list)
while max(grade_list) == b:
	t = len(grade_list)
	for i in range(t):
		if grade_list[i] == b:
			del grade_list[i]
			break
c = max(grade_list)
print(a, b, c) 