from collections.abc import Iterator

class SequenceIterator(Iterator):
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0
    
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration