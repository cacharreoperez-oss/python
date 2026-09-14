class InfiniteList:
    def __init__(self, *values, fill_value=None):
        self.fill_value = fill_value
        self.items = list(values)
        self.content = self.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.items) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step

            if start < 0:
                start += len(self.items)
            if stop < 0:
                stop += len(self.items)

            result = []
            for i in range(start, stop, step):
                if i < 0:
                    result.append(self.fill_value)
                elif i >= len(self.items):
                    result.append(self.fill_value)
                else:
                    result.append(self.items[i])
            return result

        if index < 0:
            index += len(self.items)

        if index < 0 or index >= len(self.items):
            raise IndexError('list index out of range')

        return self.items[index]

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            raise TypeError('slice assignment not supported')

        if index < 0:
            index += len(self.items)

        if index >= len(self.items):
            self.items.extend([self.fill_value] * (index - len(self.items) + 1))

        self.items[index] = value

    def __str__(self):
        return ','.join(str(item) for item in self.items)

