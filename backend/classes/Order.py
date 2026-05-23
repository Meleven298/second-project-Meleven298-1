from datetime import datetime


class Order:
    """Класс заказа."""
    
    def __init__(self, order_id: int, products: list, customer) -> None:
        '''Конструктор класса заказа.

        Args:
            order_id: Айди заказа.
            products: Продукты.
            customer: Покупатель.
        '''

        self.__id = order_id
        self.__customer = customer
        self.__products = products
        self.__total_cost = sum(p.get_cost() for p in products)
        self.__date = datetime.now()
        self.__status = "completed"
    
    def get_id(self):
        '''Геттер для айди.
        
        Returns:
            self.__id: Айди заказа.
        '''

        return self.__id
    
    def get_customer(self):
        '''Геттер для покупателя в заказе.
        
        Returns:
            self.__customer: Имя покупателя в заказе.
        '''

        return self.__customer
    
    def get_products(self):
        '''Геттер для продукта.
        
        Returns:
            self.__products: Список продуктов.
        '''

        return self.__products
    
    def get_total_cost(self):
        '''Геттер для итоговой цены.
        
        Returns:
            self.__total_cost: Итоговоая цена.
        '''

        return self.__total_cost
    
    def return_order(self):
        '''Возвращение заверщенного статуса заказа.'''

        self.__status = "returned"
    