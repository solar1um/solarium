# dunder method, magic methods
# double underscore methods
# isistence

print(dir(1), type(1))


class CInt:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return f'sum is {self.n + other}'

    def __eq__(self, other):
        if self.n == other:
            return f'{self.n}, is equal to {other}'
        else:
            return f'{self.n} is not equal to {other}'

#   not equal
    def __ne__(self, other):
        if self.n != other:
            return f'{self.n} is not equal to {other}'
        else:
            return f'{self.n} is equal to {other}'

    def __str__(self):
        return f'number is {self.n}'

    def __repr__(self):
        return f'number issaafd {self.n}'

c = CInt(5)

# print(c + 10)
# print(c == 10)
# print(c != 5)
print(c)
print(repr(c.n))