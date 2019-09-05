class RangeIterator:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        curr = self.current
        if curr >= self.stop:
            raise StopIteration
        self.current += 1
        return curr
