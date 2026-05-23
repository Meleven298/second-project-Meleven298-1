import random


class Employee:
    '''Класс Рабочего.'''

    def __init__(self, position):
        '''Конструктор класса рабочего.
        
        Args:
            position: Должность рабочего.
        '''

        self.id = random.randint(1,1000000000)
        self.position = position
    