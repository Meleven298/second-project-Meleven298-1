class Company:
    '''Класс компании.'''

    def __init__(self):
        '''Конструктор класса компании.'''

        self.net_worth = 0
        self.header = 'Valeev Marsel'

    def get_header(self):
        """Геттер для директора.
        
        Returns:
            self.header: Имя текущего директора.
        """
        
        return self.header
    
    def set_header(self, new_header: str):
        """Сеттер для директора.

        Args:
            new_header: Имя директора.
        """

        self.header = new_header
    