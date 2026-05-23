class Customer:
    """Класс покупателя"""
    
    def __init__(self, name: str, phone: str) -> None :
        '''Конструктор класса Покупателя.
        
        Args:
            name: Имя покупателя.
            phone: Телефон покупателя.
        '''

        self.__name = name
        self.__phone = phone
        self.__purchase_history = []
    
    def get_name(self) -> str:
        '''Геттер для имени.
        
        Returns:
            self.__name: Имя покупателя.
        '''

        return self.__name
    
    def get_phone(self) -> str:
        '''Сеттер для покупателя:
        
        Returns:
            self.__phone: Телефон покупателя.
        '''

        return self.__phone
    
    def add_purchase(self, product_name: str, cost: float) -> None:
        '''Функция для добавления покупки.
        
        Args:
            product_name: Имя продукта.
            cost: Цена продукта.
        '''

        self.__purchase_history.append({"product": product_name, "cost": cost})
    
    def get_purchase_history(self):
        '''Геттер для истории покупок.
        
        Returns:
            self.__purchase_history: Имя покупателя.
        '''

        return self.__purchase_history
    