from backend.classes.Order import Order
from backend.classes.SalesPoint import SalesPoint
from backend.classes.Product import Product
from backend.classes.Customer import Customer
from backend.classes.Company import Company
from backend.classes.Storage import Storage
from datetime import datetime
from typing import Optional


class SalesOperations:
    '''Класс операций над продажами.'''
    
    @staticmethod
    def sell_product(sales_point: SalesPoint, product: Product, customer: Customer, company: Company) -> Optional[Order]:
        """Продажа товара в пункте продаж.
        
        Args:
            sales_point: Точка продаж.
            product: Продаваемый продукт.
            customer: Покуптель.
            company: Компания.

        Returns:
            order: Обьект заказ либо None.
        """
        
        result: Optional[Order] = None

        if not sales_point.is_open():
            print("Пункт продаж закрыт!")
        else:
            found = False
            
            for cell in sales_point.get_cells():
                for prod in cell.get_products():
                    if prod.get_id() == product.get_id() and found is False:
                        cell.delete_product(product)
                        sales_point.add_revenue(product.get_cost())
                        company.net_worth += product.get_cost()
                        customer.add_purchase(product.get_name(), product.get_cost())

                        print(f"Продан товар {product.get_name()} за {product.get_cost()} руб.")

                        result = Order(datetime.now().timestamp(), customer, [product])
                        found = True
            
            if found is False:
                print("Товар не найден в пункте продаж")

        return result
    
    @staticmethod
    def return_product(sales_point: SalesPoint, order: Order, company: Company, storage: Storage) -> bool:
        """Возврат товара.
        
        Args:
            sales_point: Точка продаж.
            order: Заказ.
            company: Компания.
            storage: Склад.
        
        Returns:
            True или False в зависимости от успешности возврата.
        """
        
        result = False

        if order.get_status() == "returned":
            print("Товар уже был возвращен")
        else:
            for product in order.get_products():
                try:
                    storage.add_product(product)
                    company.net_worth -= product.get_cost()
                    sales_point.add_revenue(-product.get_cost())

                    print(f"Возврат товара {product.get_name()}")

                    result = True
                except IndexError:
                    print(f"Нет места на складе, товар {product.get_name()} утилизирован")

                    company.net_worth -= product.get_cost()
                    result = True
            
            if result is True:
                order.return_order()

        return result
    