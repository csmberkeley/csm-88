class Range:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return RangeIterator(self.stop)
