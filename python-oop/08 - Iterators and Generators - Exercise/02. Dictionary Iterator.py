class dictionary_iter:
    def __init__(self, d) -> None:
        self.data = d
        self.__data = iter(self.data.items())

    def __iter__(self):
        self.__data = iter(self.data.items())
        return self

    def __next__(self):
        return next(self.__data)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
