class countdown_iterator:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 0:
            i = self.count
            self.count -= 1
            return i
        raise StopIteration

# test code
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")

