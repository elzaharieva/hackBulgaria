import unittest
from crash_desk import Bill
		

class BillTest(unittest.TestCase):

	def setUp(self):
		self.my_bill=Bill(5)

	def test_create_new_bill_instance(self):
		self.my_bill.amount = 15 #samo za tazi funkciq se promenq na 15
		self.assertTrue(isinstance(self.my_bill, Bill)) #Dali my_bill e ot tip Bill

	def test_valid_amount(self):
		self.assertEqual(self.my_bill.amount, 5) #Dali my_bill.amount == 5

	def test_int_cast(self):
		self.assertEqual(int(self.my_bill), 5)

	def test_str_cast(self):
		self.assertEqual(str(self.my_bill), 'A 5$ bill')

	def test_eq(self):
		my_other_bill=Bill(5)
		self.assertTrue(self.my_bill == my_other_bill)

if __name__=="__main__":
	unittest.main()