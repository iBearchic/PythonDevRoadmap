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
        """ 
        Наглядно показана суть dunder-getitem
        Вследствие реализации специальных методов __len__ и __getitem__ класс
        FrenchDeck ведет себя, как стандартная последовательность, и позволяет использовать базовые средства языка
        """
        
        return self._cards[position]