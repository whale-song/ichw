#lab8(2).py\
data = {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4, 'd': {'xy': 5, 'yz': 6}}

class flatten:
	def __init__(self, dictionary):
		self.d = dictionary
		self.keys = list(dictionary.keys())
		self.targets = list(filter(self.judge_element, self.keys))  #self.targets: ['b','d']
		flattened_dicts = list(map(self.flatten_dict, self.targets))
		for i in flattened_dicts:
			self.d.update(i)
		for i in self.targets:
			del self.d[i]
		print(self.d)


	def judge_element(self, key):
		return type(self.d[key]) == dict

	def flatten_dict(self, target):
		flatten_keys = [(target+'.'+i) for i in self.d[target].keys()]
		return dict(zip(flatten_keys, self.d[target].values()))

if __name__ == '__main__':
	flatten(data)