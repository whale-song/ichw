from functools import *

people = [{'name': 'Mary', 'height': 160},
		  {'name': 'Isla', 'height': 80},
		  {'name': 'Sam'}]

def height_in(x):
	return 'height' in x

def add_height(x, y):
	return x + y

def extract_height(x):
	return x['height']

heights = list(
	map(
		extract_height,
		list(filter(height_in, people))
		)
	)
height_total = reduce(add_height, heights)
print(height_total / len(heights))