import unittest
from crash_desk import BatchBill
from crash_desk import Bill

class TestBatchBill(unittest.TestCase):

	def setUp(self):
		self.values = [10, 20, 50, 100]
		self.bills = [Bill(value) for value in self.values]
		self.my_batch = BatchBill(self.bills)

	def test_init(self):
		self.assertTrue(isinstance(self.my_batch, BatchBill))
		self.assertEqual(self.my_batch.batch, self.bills)

	def test_indexation(self):
		self.assertEqual(self.my_batch[1], self.bills[1])

if __name__=="__main__":
	unittest.main()