from .StorageCell import StorageCell

class SalesPoint:
    """Пункт продаж"""
    
    def __init__(self, id: int, address: str) -> None:
        '''Конструктор класса точки продажи.
        
        Args:
            id: Айди точки продаж.
            address: Адрес точки продаж.
        '''

        self.__id = f"SP_{id}"
        self.__address = address
        self.__cells = [StorageCell(i + 100) for i in range(5)]
        self.__revenue = 0
        self.__is_open = True
    
    def get_id(self) -> int:
        '''Геттер для айди.
        
        Returns:
            self.__id: Айди точки продаж.
        '''

        return self.__id
    
    def get_address(self) -> str:
        '''Геттер для адресс.
        
        Returns:
            self.__address: Адресс точки продаж.
        '''

        return self.__address
    
    def get_cells(self) -> list:
        '''Геттер для ячеек
        
        Returns:
            self.__cells: Список ячеек точки продаж.
        '''

        return self.__cells
    
    def get_revenue(self) -> int:
        '''Геттер для выручки.
        
        Returns:
            self.__revenue: Выручка точки продаж.
        '''

        return self.__revenue
    
    def add_revenue(self, amount: float) -> None:
        '''Добавить выручку.
        
        Args:
            amount: Добавляемая выручка.
        '''

        self.__revenue += amount
    
    def is_open(self) -> None:
        '''Открыта ли точка продаж.
        
        Returns:
            self.__is_open: Открыто или не открыто.
        '''

        return self.__is_open
    
    def close(self) -> None:
        '''Закрытие точки продаж.'''

        self.__is_open = False
    
    def open(self) -> None:
        '''Открытие точки продаж.'''

        self.__is_open = True
