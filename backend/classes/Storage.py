from .StorageCell import StorageCell
from .Product import Product

class Storage:
    '''Класс склада.'''

    def __init__(self, storage_id: int = 1):
        '''Конструктор класса склада.
        
        Args:
            storage_id: Айди склада.
        '''

        self.id = f"STORAGE_{storage_id}"
        self.cells = [StorageCell(i + (storage_id-1)*10) for i in range(1, 11)]

    def get_id(self):
        '''Геттер для айди.
        
        Returns:
            self.id: Айди склада.
        '''

        return self.id

    def get_cells(self):
        '''Геттер для ячеек.
        
        Returns:
            self.cells: Список ячеек.
        '''

        return self.cells

    def add_product(self, product: Product):
        '''Добавить продукт.
        
        Args:
            product: Экземпляр класса Product.

        Returns: 
            True в случае если продукт добавлен.
        
        Raises:
            IndexError если нету свободных ячеек на складе.
        '''

        for cell in self.cells:
            if cell.add_product(product):
                product.set_storage(self.id)

                print(f"Продукт {product.get_name()} успешно добавлен в ячейку {cell.get_id()}")

                return True
            
        raise IndexError("Нет свободных ячеек на складе!")

    def get_all_products(self):
        '''Получить все продукты.
        
        Returns:
            products: Список всех продуктов на складе.
        '''

        products = []

        for cell in self.cells:
            products.extend(cell.get_products())

        return products
    
    def get_total_volume(self):
        '''Получть занятый обьем:
        
        Returns:
            Сумма всех обьемов в каждой ячейке.
        '''

        return sum(cell.current_capacity for cell in self.cells)
    