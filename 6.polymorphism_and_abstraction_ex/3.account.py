from typing import List, Optional


class Account:
    def __init__(self, owner: str, amount: Optional[int] = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: List = []
        self.__starting_amount = amount

    def handle_transaction(self, transaction_amount: int):
        if self.amount + transaction_amount < 0:
            raise ValueError('sorry cannot go in debt!')
        self.amount += transaction_amount
        self._transactions.append(transaction_amount)
        return f'New balance: {self.amount}'

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self.handle_transaction(amount)

    @property
    def balance(self):
        return self.__starting_amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.__starting_amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.__starting_amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return [self._transactions[tr] for tr in range(len(self._transactions)-1, -1, -1)]

    def __eq__(self, other):
        return True if self.amount == other.amount else False

    def __gt__(self, other):
        return True if self.amount > other.amount else False

    def __lt__(self, other):
        return True if self.amount < other.amount else False

    def __le__(self, other):
        return True if self.amount <= other.amount else False

    def __ge__(self, other):
        return True if self.amount >= other.amount else False

    def __ne__(self, other):
        return True if self.amount != other.amount else False

    def __add__(self, other):
        new_acc =  Account(f'{self.owner}&{other.owner}', self.amount + other.amount)
        new_acc._transactions = self._transactions + other._transactions
        new_acc.__starting_amount = self.__starting_amount + other.__starting_amount
        return new_acc


# Test code!
acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)

