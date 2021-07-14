from typing import List
import unittest


class Account:
    owner: str
    amount: int
    _transactions: List[int]

    def __init__(self, owner: str, amount: int = 0) -> None:
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self) -> int:
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account: 'Account', amount_to_add) -> str:
        if account.balance + amount_to_add < 0:
            raise ValueError('sorry cannot go in debt!')

        account.add_transaction(amount_to_add)
        return f'New balance: {account.balance}'

    def __str__(self) -> str:
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, key: int) -> int:
        return self._transactions[key]

    def __eq__(self, o: 'Account') -> bool:
        return self.balance == o.balance

    def __ne__(self, o: 'Account') -> bool:
        return self.balance != o.balance

    def __lt__(self, o: 'Account') -> bool:
        return self.balance < o.balance

    def __gt__(self, o: 'Account') -> bool:
        return self.balance > o.balance

    def __le__(self, o: 'Account') -> bool:
        return self.balance <= o.balance

    def __ge__(self, o: 'Account') -> bool:
        return self.balance >= o.balance

    def __add__(self, o: 'Account') -> 'Account':
        new_name = f'{self.owner}&{o.owner}'
        new_amount = self.amount + o.amount
        new_account = self.__class__(new_name, new_amount)
        new_transactions = self._transactions + o._transactions
        for t in new_transactions:
            new_account.add_transaction(t)
        return new_account


class AccountTests(unittest.TestCase):
    def test_account_can_be_initalized(self):
        acc = Account('bob', 10)
        self.assertEqual('bob', acc.owner)
        self.assertEqual(10, acc.amount)

    def test_account_can_be_initialized_without_amount(self):
        acc2 = Account('john')
        self.assertEqual('john', acc2.owner)
        self.assertEqual(0, acc2.amount)

    def test_account_has_valid_str_representation(self):
        acc = Account('bob', 10)
        expected_value = 'Account of bob with starting amount: 10'
        actual_value = str(acc)
        self.assertEqual(expected_value, actual_value)

    def test_account_has_correct_repr_representation(self):
        acc = Account('bob', 10)
        expected_value = 'Account(bob, 10)'
        actual_value = repr(acc)
        self.assertEqual(expected_value, actual_value)

    def test_account_can_add_valid_transaction(self):
        acc = Account('bob', 10)
        expected_value = [20]
        acc.add_transaction(20)
        actual_value = acc._transactions
        self.assertEqual(expected_value, actual_value)

    def test_account_raises_ValueError_when_adding_str_transaction(self):
        acc = Account('bob', 10)
        with self.assertRaises(ValueError) as exc:
            acc.add_transaction('')
        expected_value = 'please use int for amount'
        actual_value = str(exc.exception)
        self.assertEqual(expected_value, actual_value)

    def test_account_raises_ValueError_when_adding_float_transaction(self):
        acc = Account('bob', 10)
        with self.assertRaises(ValueError) as exc:
            acc.add_transaction(0.5)
        expected_value = 'please use int for amount'
        actual_value = str(exc.exception)
        self.assertEqual(expected_value, actual_value)

    def test_account_after_adding_valid_transaction_balance_updates(self):
        acc = Account('bob', 10)
        expected_value = 30
        acc.add_transaction(20)
        actual_value = acc.balance
        self.assertEqual(expected_value, actual_value)

    def test_validate_transaction_method(self):
        acc = Account('bob', 10)
        with self.assertRaises(ValueError) as exc:
            Account.validate_transaction(acc, -20)
        expected_value = 'sorry cannot go in debt!'
        actual_value = str(exc.exception)
        self.assertEqual(expected_value, actual_value)

    def test_account_can_add_multiple_transactions(self):
        acc = Account('bob', 10)
        acc.add_transaction(20)
        acc.add_transaction(-20)
        acc.add_transaction(30)
        expected_value = 40
        actual_value = acc.balance
        self.assertEqual(expected_value, actual_value)

    def test_account_can_be_iterated(self):
        acc = Account('bob', 10)
        acc.add_transaction(20)
        acc.add_transaction(-20)
        acc.add_transaction(30)
        expected_value = '20\n-20\n30'
        actual_value = '\n'.join(map(str, (t for t in acc)))
        self.assertEqual(expected_value, actual_value)

    def test_two_accounts_can_be_compared_correctly(self):
        acc = Account('bob', 10)
        acc.add_transaction(20)
        acc.add_transaction(-20)
        acc.add_transaction(30)
        acc2 = Account('john')
        acc2.add_transaction(10)
        acc2.add_transaction(60)
        expected_value = 'False\nFalse\nTrue\nTrue\nFalse\nTrue'

        actual_value = '\n'.join(map(str,
                                     (acc > acc2, acc >= acc2, acc < acc2,
                                      acc <= acc2, acc == acc2, acc != acc2)))
        self.assertEqual(expected_value, actual_value)

    def test_two_accounts_can_be_added(self):
        acc = Account('bob', 10)
        acc.add_transaction(20)
        acc.add_transaction(-20)
        acc.add_transaction(30)
        acc2 = Account('john')
        acc2.add_transaction(10)
        acc2.add_transaction(60)
        acc3 = acc + acc2
        expected_value = 'Account of bob&john with starting amount: 10\n[20, -20, 30, 10, 60]'
        actual_value = str(acc3) + '\n' + str(acc3._transactions)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()
