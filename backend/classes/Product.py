class Product:
    '''Класс товара.'''

    def __init__(self, id: int = 0, name: str = 'NoName', cost: int = 0, volume: int = 1) -> None:
        '''Конструктор для класс продукта.
        
        Args:
            id: Айди продукта.
            name: Имя продукта.
            cost: Цена продукта.
            volume: Объем продукта.
        '''
        
        self.__id = id
        self.__name = name
        self.__cost = cost
        self.__volume = volume
        self.__storage = None

    def get_id(self) -> int:
        '''Геттер для айди.
        
        Returns:
            self.__id: Айди продукта.
        '''

        return self.__id
    
    def get_name(self) -> str:
        '''Геттер для имени.
        
        Returns:
            self.__name: Имя продукта.
        '''

        return self.__name

    def get_cost(self) -> int:
        '''Геттер для цены.
        
        Returns:
            self.__cost: Цена продукта.
        '''

        return self.__cost

    def get_volume(self) -> int:
        '''Геттер для объем.
        
        Returns:
            self.__volume: Объем продукта.
        '''

        return self.__volume

    def get_storage(self):
        '''Геттер для склада.
        
        Returns:
            self.__storage: Узнать склад.
        '''
        return self.__storage

    def set_storage(self, storage):
        '''Сеттер для склада.
        
        Args:
            storage: Новый склад.
        '''

        self.__storage = storage

    def __str__(self):
        '''Строковое представление класса продукта.
        
        Returns:
            Строковое представление класса продукта.
        '''

        return f"{self.__name} (ID:{self.__id}) - {self.__cost} руб."
    