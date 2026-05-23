from backend.classes.Company import Company
from backend.classes.Product import Product
from backend.classes.StorageCell import StorageCell
from backend.classes.Storage import Storage
from backend.classes.SalesPoint import SalesPoint

import json


class ProductOperations:
    '''Класс операций над продуктами.'''

    def transfer_good(self, product: Product, storage_cell: StorageCell) -> None:
        '''Перенос товара в ячейку.
        
        Args:
            product: Экземпляр класса Product.
            storage_cell: Экземпляр класса ячейки склада.
        
        Returns:
            None
        '''

        try:
            storage_cell.add_product(product)
            product.set_storage(storage_cell)

            print(f'Товар {product.get_name()} успешно перенесен в ячейку {storage_cell.get_id()}')
        except:
            print('Ячейка уже переполнена. Выберите другую.')
    
    def sell_product(self, company: Company, product: Product, storage_cell: StorageCell) -> None:
        '''Продажа продукта.
        
        Args:
            company: Экземпляр класса Company.
            product: экземпляр класса Product.
            storage_cell: Экземпляр класса ячейки склада.
        
        Returns:
            None
        '''

        storage_cell.delete_product(product)
        company.net_worth += product.get_cost()
    
    def refund_product(self, company: Company, product: Product, storage: Storage) -> None:
        '''Возврат продукта.
        
        Args:
            company: Экземпляр класса Company.
            product: экземпляр класса Product.
            storage: Экземпляр класса Storage.
        
        Returns:
            None
        '''

        try:
            storage.add_product(product)
        except IndexError:
            print('Нет свободных ячеек. Товар утилизирован')

        company.net_worth -= product.get_cost()
    
    def transfer_to_sales_point(self, sales_point: SalesPoint, storage: Storage, product: Product) -> bool:
        """Перемещение товара со склада в пункт продаж.

        Args:
            sales_point: Точка продажи.
            storage: Экземпляр класса Storage.
            product: экземпляр класса Product.

        Returns:
            True или False.
        """
        result = False
        
        for cell in storage.get_cells():
            for prod in cell.get_products():
                if prod.get_id() == product.get_id() and result is False:
                    cell.delete_product(product)

                    for sp_cell in sales_point.get_cells():
                        if sp_cell.add_product(product) and result is False:
                            print(f"✅ Товар {product.get_name()} перемещен в {sales_point.get_id()}")

                            result = True
                    
                    if result is False:
                        cell.add_product(product)

                        print("❌ Нет места в пункте продаж")

                        result = False
                
        if result is False:
            print("❌ Товар не найден на складе")

        return result


def load_catalog(filename: str = "products.json") -> list[dict]:
    """Загружает каталог из файла.
    
    Args:
        filename: "products.json".
    
    Returns:
        Каталог json, либо пустой список.
    """

    result = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            result = json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")

        result = []

    return result


def buy_products(storage: Storage, company: Company, cart_items: list[tuple[dict, int]]) -> tuple[bool, float, str]:
    """
    Логика закупки.
    
    Args:
        storage: Экземпляр класса Storage.
        company: Экземпляр класса Company.
        cart_items: Корзина покупок.
    
    Returns:
        success: Статус успешной покупки.
        total_cost: Итоговая цена.
        message: Сообщение об успешности.
    """

    success = False
    total_cost = 0
    message = ""

    if not cart_items:
        message = "Корзина пуста"

        return success, total_cost, message

    for product_data, quantity in cart_items:
        total_cost += product_data["цена"] * quantity

    if total_cost > company.net_worth:
        message = f"Недостаточно средств. Нужно: {total_cost:.2f}, доступно: {company.net_worth:.2f}"

        return success, total_cost, message

    company.net_worth -= total_cost

    products_created = 0
    failed_products = 0
    
    for product_data, quantity in cart_items:
        for _ in range(quantity):
            product = Product(
                id=product_data["id"],
                name=product_data["название"],
                cost=product_data["цена"],
                volume=product_data["объём"]
            )
            
            try:
                storage.add_product(product)

                products_created += 1
            except IndexError:
                company.net_worth += product.get_cost()
                failed_products += 1
    
    success = True
    message = f"Закупка завершена. Создано {products_created} товаров"
    
    if failed_products > 0:
        message += f", {failed_products} утилизировано (не было места)"

    products = storage.get_all_products()
    
    for product in products:
        print(product)
    
    return success, total_cost, message
