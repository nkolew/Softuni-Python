from functools import reduce
import operator


class Calculator:

    @staticmethod
    def add(*args):
        return reduce(operator.add, args)

    @staticmethod
    def multiply(*args):
        return reduce(operator.mul, args)

    @staticmethod
    def divide(*args):
        return reduce(operator.truediv, args)

    @staticmethod
    def subtract(*args):
        return reduce(operator.sub, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
