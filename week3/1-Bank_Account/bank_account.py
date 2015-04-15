class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.hist = ['Account was created']

    def deposite(self, amount):
        if amount < 0:
            raise ValueError
        self.balance += amount
        self.hist.append('Deposited {}{}'.format(amount, self.currency))

    def balance1(self):
        self.hist.append(
            'Balance check -> {}{}'.format(self.balance, self.currency))
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.hist.append(
                '{}{} was withdrawed'.format(amount, self.currency))
            return True
        else:
            self.hist.append(
                'withdraw for {}{} failed'.format(amount, self.currency))
            return False

    def __str__(self):
        return ('Bank account for {} with balance of {}{}'.format(self.name, self.balance, self.currency))

    def __int__(self):
        self.hist.append(
            '__int__ check -> {}{}'.format(self.balance, self.currency))
        return self.balance

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            self.hist.append(
                'Failed to transfer {}{} to {}'.format(amount, self.currency, account.name))
            account.hist.append(
                'Failed to transfer {}{} from {}'.format(amount, self.currency, self.name))
            raise ValueError

        if self.balance < amount:
            self.hist.append(
                'Failed to transfer {}{} to {}'.format(amount, self.currency, account.name))
            account.hist.append(
                'Failed to transfer {}{} from {}'.format(amount, self.currency, self.name))
            return False

        self.balance -= amount
        account.balance += amount
        self.hist.append(
            'Transer to {} for {}{}'.format(account.name, amount, self.currency))
        account.hist.append(
            'Transfer from {} for {}{}'.format(self.name, amount, account.currency))
        return True

    def history(self):
        return self.hist
