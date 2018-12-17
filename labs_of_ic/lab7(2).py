dictionary = {
	'sir': 'matey', 'hotel': 'feabag inn', 'student': 'swabble',
	'boy': 'matey', 'madam': 'proud beauty', 'professor': 'foul blaggart',
	'restaurant': 'galley', 'your': 'yer', 'excuse': 'arr',
	'students': 'swabbles', 'are': 'be', 'lawyer': 'foul blaggart',
	'the': 'th\'', 'restroom': 'head', 'my': 'me',
	'hello': 'avast', 'is': 'be', 'man': 'matey'
	}

source = input().split()
a = ''
for i in source:
	a += dictionary[i] + ' '
print(a)



'''
output = []
for i in source:
	if dictionary.__contains__(i) == True:
		output.append(dictionary[i])
	else:
		output.append(i)
print(''.join(output))
'''