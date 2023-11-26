class sequence_repeat:
    def __init__(self, sequence: str, num: int):
        self.sequence = sequence
        self.num = num
        self.result = ''
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > 0:
            i = self.i
            if self.i < len(self.sequence):
                self.i += 1
            else:
                i = 0
                self.i = 1
            self.num -= 1
            return self.sequence[i]
        raise StopIteration


# test code!
result = sequence_repeat('abc', 8)
for item in result:
    print(item, end='')
print()
print('-----------------------')
result = sequence_repeat('I Love Python', 8)
for item in result:
    print(item, end='')
