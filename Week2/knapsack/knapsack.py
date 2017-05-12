
class KnapSack(object):
	"""docstring for KnapSack"""
	def __init__(self, item_count, capacity, items):
		self.item_count = item_count
		self.knapsack_capacity = capacity
		self.items = items
		self.taken = [0] * (len(self.items) + 1)

		self.weights_list = map(lambda x: x.weight, self.items)
		self.value_list = map(lambda x: x.value , self.items)

	def generate_table(self):
		self.table = [[0 for x in xrange(self.knapsack_capacity + 1)] for y in xrange(self.item_count + 1)]
		for i in xrange(1, len(self.value_list) + 1):
			item_index = i - 1
			for j in xrange(1, self.knapsack_capacity + 1):
				if( j - self.weights_list[item_index] < 0):
					self.table[i][j] = self.table[i-1][j]
				else:
					self.table[i][j] = max(self.table[i-1][j], self.value_list[item_index] + self.table[item_index][j-self.weights_list[item_index]])

	def generate_solution(self):
		self.optimal_value = self.table[self.item_count][self.knapsack_capacity]
		weight = self.knapsack_capacity
		for i in xrange(self.item_count, 0, -1):
			if(self.table[i][weight] != self.table[i-1][weight]):
				self.taken[i] = 1
				weight -= self.weights_list[i-1]
			else:
				self.taken[i] = 0

	def get_solution(self):
		output_data = None
		output_data = str(self.optimal_value) + ' ' + str(1) + '\n'
		output_data += ' '.join(map(str, self.taken[1:]))
		return output_data







		