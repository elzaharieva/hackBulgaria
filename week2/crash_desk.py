class Bill:
	def __init__(self, amount):
		self.amount=amount

	def __str__(self):
		return "A {}$ bill".format(self.amount)

	def __repr__(self):
		return self.__str__()

	def __int__(self):
		return self.amount

	def __eq__(self, other):
		return self.amount==other.amount

	def __hash__(self):
		return hash(str(self.amount))




class BatchBill():

	def __init__(self, batch):
		self.batch=batch

	def __len__(self):
		return len(self.batch)

	def total(self):
		return sum(self.batch)

	def __getitem__(self, index):
		return self.batch[index]

class CashDesk():

	def __init__(self):
		self.money=[]

	def take_money(self, money):
		if isinstance (money, Bill):
			self.money.append(money)
		else:
			for m in money:
				(self.money).append(m)
		return self.money

	def total(self):
		suma=0
		for money in self.money:
			suma+=int(money)
		return suma

	def inspect(self):
		dict={}
		for money in self.money:
			key=money
			if key in dict:
				dict[key]+=1
			else:
				dict[key]=1
		print("We have a total of {}$ in the desk".format(self.total()))
		print("We have the following count of bills, sorted in ascending order:")
		for d in dict:
			print(str(d)[2:]+"s - "+str(dict[d]))
		
		return dict
