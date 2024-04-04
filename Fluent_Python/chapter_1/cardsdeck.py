from collections import namedtuple

# namedtuple отлично подходит для создания простых классов, где не требуется определение методов
Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # использование list-comprehension здесь выглядит уместно и лаконично
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        # наглядно показана суть dunder-getitem
        # за счет данного методы мы открываем весь спектор методов над экземпляром класса FrenchDeck
        # напримеры, поиск по индексу, срезы и т.п.
        return self._cards[position]
