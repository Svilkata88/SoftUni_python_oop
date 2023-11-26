from typing import Dict


class dictionary_iter:
    def __init__(self, dictionary: Dict):
        self.dictionary = dictionary
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.dictionary):
            i = self.i
            self.i += 1
            return tuple(self.dictionary.items())[i]
        else:
            raise StopIteration

# test code
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print()

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
