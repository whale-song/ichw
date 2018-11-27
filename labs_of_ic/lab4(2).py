x = float(input())
wc = float(input())
ex = 0
n = 0
j = 1

while abs(x**(n)/(j*(n+1)))>= wc :
	if n > 0:
		j *= n
	ex += (x**n)/j
	n += 1

print(round(ex,6))
input()