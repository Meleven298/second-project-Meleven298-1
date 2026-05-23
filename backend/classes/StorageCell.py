from .Product import Product


class StorageCell:
    '''Класс ячейки склада.'''

    def __init__(self, id: int) -> None:
        '''Конструктор класса ячейки склада.
            
        Args:
            id: Айди склада.
        '''

        self.id = f'SKLD_{id}'
        self.capacity = 100
        self.current_capacity = 0
        self.products = []

    def get_id(self) -> str:
        '''Геттер для айди.
        
        Returns:
            self.id: Айди склада.
        '''

        return self.id
    
    def get_products(self) -> list:
        '''Геттер для продуктов.
        
        Returns:
            self.products: Список продуктов в ячейке.
        '''

        return self.products
    
    def add_product(self, product: Product) -> bool:
        '''Добавить продукт в ячейку.

        Args:
            product: Экземпляр класса Product.
        
        Returns:
            True или False в зависимости от успешного добавления.
        '''
        result = False
        
        if self.current_capacity + product.get_volume() <= self.capacity:
            self.products.append(product)
            self.current_capacity += product.get_volume()
            result = True

        return result

    def delete_product(self, product: Product) -> Product:
        '''Удалить продукт.
        
        Args:
            product: Удаляемый продукт.
            
        Returns:
            Удаленный продукт либо None.
        '''

        deleted_product = None
        
        for i, prod in enumerate(self.products):
            if product.get_id() == prod.get_id() and deleted_product is None:
                self.current_capacity -= prod.get_volume()
                deleted_product = self.products.pop(i)
            
        return deleted_product
    