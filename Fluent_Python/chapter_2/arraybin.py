from array import array
from random import random

# Создаем массив 
floats = array('d', (random() for i in range(10**7)))

# Пример сохранения в память
fp = open('floats.bin', 'wb')
floats.tofile(fp) 
fp.close()

# если хотим список lst перевести в массив: lst = array(lst.typecode, lst)
