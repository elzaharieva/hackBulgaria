import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.my_account = BankAccount('Rado', 1000, '$')

    def test_inst(self):
        self.assertTrue(isinstance(self.my_account, BankAccount))

    def test_deposite(self):
        self.my_account.deposite(1000)
        self.assertEqual(self.my_account.balance, 2000)
        with self.assertRaises(ValueError):
            self.my_account.deposite(-20)
        self.assertEqual(self.my_account.balance, 2000)

    def test_balance(self):
        self.assertEqual(self.my_account.balance, self.my_account.balance1())

    def test_str(self):
        need = 'Bank account for Rado with balance of 1000$'
        self.assertEqual(str(self.my_account), need)

    def test_withdraw(self):
        self.pos_amount = 30
        self.neg_amount = 2000
        self.assertTrue(self.my_account.withdraw(self.pos_amount))
        self.assertFalse(self.my_account.withdraw(self.neg_amount))

    def test_int_cast(self):
        self.assertEqual(self.my_account.balance, int(self.my_account))

    def test_transfer_different_currency(self):
        your_account = BankAccount('Koko', 50, '&')
        with self.assertRaises(ValueError):
            self.my_account.transfer_to(your_account, 200)
        self.assertEqual(self.my_account.balance, 1000)
        self.assertEqual(your_account.balance, 50)

    def test_transfer_to_move_money_than_available(self):
        your_account = BankAccount('Koko', 10, '$')
        self.assertFalse(self.my_account.transfer_to(your_account, 2000))
        self.assertEqual(self.my_account.balance, 1000)
        self.assertEqual(your_account.balance, 10)

    def test_transfer_to(self):
        your_account = BankAccount('Koko', 10, '$')
        self.assertTrue(self.my_account.transfer_to(your_account, 100))
        self.assertEqual(self.my_account.balance, 900)
        self.assertEqual(your_account.balance, 110)

        def test_history(self):
            self.assertEqual(self.my_account.hist, self.my_account.history())

if __name__ == '__main__':
    unittest.main()
