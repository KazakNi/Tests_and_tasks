class CustomList(list):
    def __init__(self, *args):
        super(CustomList, self).__init__(args)

    def __sub__(self, other):
        range_ = min(len(self), len(other))
        for i in range(range_):
            self[i] = self[i] - other[i]
        self.extend(self[range_+1:])
        return self

    def __add__(self, other):
        range_ = min(len(self), len(other))
        for i in range(range_):
            print(self[i])
            self[i] = self[i] + other[i]
        self.extend(self[range_+1:])
        return self


class MyClass(type):
    def __new__(cls, name, basename, attrs):
        private_attrs = {attr if attr.startswith('__') else 'custom_' + attr:
                         v for attr, v in attrs.items()}
        return super().__new__(cls, name, basename, private_attrs)


class CustomClass(metaclass=MyClass):
    def __init__(self, val=100) -> None:
        self.val = val

    @classmethod
    def lol(self):
        print('hi')

