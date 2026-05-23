from backend.ProductOperations import ProductOperations, load_catalog
from backend.StaffOperations import StaffOperations
from backend.StorageOperations import StorageOperations
from backend.SalesOperations import SalesOperations
from backend.InfoOperations import InfoOperations
from backend.classes.Company import Company
from backend.classes.Customer import Customer
from backend.classes.Employee import Employee
from backend.classes.SalesPoint import SalesPoint
from frontend.buy_catalog import run_purchase_ui
from backend.DataStorage import DataStorage

import sys
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class CRM:
    def __init__(self) -> None:
        """Конструктор класса CRM."""
        
        self.company = Company()
        self.storages = []
        self.sales_points = []
        self.employees = []
        self.customers = []
        self.orders = []
        self.product_ops = ProductOperations()
        self.staff_ops = StaffOperations()
        self.storage_ops = StorageOperations()
        self.sales_ops = SalesOperations()
        self.info_ops = InfoOperations()

        self.load_data()

        try:
            self.catalog = load_catalog("products.json")
        except:
            self.catalog = []
    
    def load_data(self) -> None:
        '''Загружает все данные.'''

        data = DataStorage.load("crm_data.json", {})
        
        self.company.net_worth = data.get("net_worth", 1000000)
        self.orders = data.get("orders", [])
        
        sales_points_data = data.get("sales_points", [])
        
        for sp_data in sales_points_data:
            sp = SalesPoint(sp_data["id"], sp_data["address"])
            self.sales_points.append(sp)
        
        print(f"✅ Загружено. Баланс: {self.company.net_worth:.2f} руб.")
    
    def save_data(self) -> None:
        '''Сохраняет все данные.'''

        sales_points_data = []
        
        for sp in self.sales_points:
            sales_points_data.append({
                "id": sp.get_id(),
                "address": sp.get_address(),
                "revenue": sp.get_revenue()
            })
        
        data = {
            "net_worth": self.company.net_worth,
            "sales_points": sales_points_data,
            "orders": self.orders
        }
        
        DataStorage.save("crm_data.json", data)

        print("💾 Данные сохранены")

    def display_menu(self) -> None:
        """Отображение главного меню."""

        print("\n" + "=" * 70)
        print(" ГЛАВНОЕ МЕНЮ CRM СИСТЕМЫ".center(70))
        print("=" * 70)
        
        print("\n📦 ОПЕРАЦИИ С ТОВАРАМИ:")
        print("   1.  Перемещение товаров (склад->склад)")
        print("   2.  Перемещение товаров (склад->пункт продаж)")
        print("   3.  Продажа товара")
        print("   4.  Возврат товара")
        print("   5.  Закупка товара")
        
        print("\n👥 УПРАВЛЕНИЕ ПЕРСОНАЛОМ:")
        print("   6.  Найм сотрудника")
        print("   7.  Увольнение сотрудника")
        print("   8.  Смена ответственного лица")
        
        print("\n🏢 УПРАВЛЕНИЕ ОБЪЕКТАМИ:")
        print("   9.  Открытие склада")
        print("   10. Закрытие склада")
        print("   11. Открытие пункта продаж")
        print("   12. Закрытие пункта продаж")
        
        print("\n📊 ИНФОРМАЦИЯ И ОТЧЕТЫ:")
        print("   13. Информация о складе")
        print("   14. Информация о пункте продаж")
        print("   15. Товары на складе")
        print("   16. Товары на пункте продаж")
        print("   17. Товары доступные к закупке")
        print("   18. Доходность предприятия")
        
        print("\n" + "-" * 70)
        print("   0.  Сохранить и выйти")
        print("=" * 70)
    
    def run(self) -> None:
        """Запуск приложения."""

        program_active = True

        while program_active:
            self.display_menu()

            choice = input("\nВыберите действие: ").strip()
            
            if choice == "1":
                self.transfer_storage_to_storage()
            elif choice == "2":
                self.transfer_to_sales_point()
            elif choice == "3":
                self.sell_product()
            elif choice == "4":
                self.return_product()
            elif choice == "5":
                self.buy_products_ui()
            elif choice == "6":
                self.hire_employee()
            elif choice == "7":
                self.fire_employee()
            elif choice == "8":
                self.change_header()
            elif choice == "9":
                self.open_storage()
            elif choice == "10":
                self.close_storage()
            elif choice == "11":
                self.open_sales_point()
            elif choice == "12":
                self.close_sales_point()
            elif choice == "13":
                self.storage_info()
            elif choice == "14":
                self.sales_point_info()
            elif choice == "15":
                self.storage_products()
            elif choice == "16":
                self.sales_point_products()
            elif choice == "17":
                self.show_available_products()
            elif choice == "18":
                self.company_profit()
            elif choice == "0":
                self.save_and_exit()
                program_active = False
            else:
                print("Неверный выбор!")
    
    def transfer_storage_to_storage(self) -> None:
        """Перемещение между складами."""

        if len(self.storages) >= 2:
            print("Доступные склады:")

            for i, s in enumerate(self.storages):
                print(f"  {i+1}. {s.get_id()}")
            
            try:
                from_idx = int(input("Из какого склада? ")) - 1
                to_idx = int(input("В какой склад? ")) - 1
                
                products = self.storages[from_idx].get_all_products()

                if products:
                    print("Товары:")

                    for i, p in enumerate(products):
                        print(f"  {i+1}. {p}")
                    
                    prod_idx = int(input("Какой товар? ")) - 1
                    product = products[prod_idx]
                    
                    transfer_done = False
                    
                    for cell in self.storages[from_idx].get_cells():
                        for prod in cell.get_products():
                            if prod.get_id() == product.get_id() and transfer_done is False:
                                cell.delete_product(product)

                                try:
                                    self.storages[to_idx].add_product(product)

                                    print(f"✅ Товар перемещен в {self.storages[to_idx].get_id()}")

                                    transfer_done = True
                                except IndexError:
                                    cell.add_product(product)

                                    print("Нет места в целевом складе")

                                    transfer_done = True
                else:
                    print("Нет товаров")
            except:
                print("Ошибка")
        else:
            print("Нужно минимум 2 склада")
    
    def transfer_to_sales_point(self) -> None:
        """Перемещение со склада в пункт продаж."""
        
        result = None

        if not self.storages:
            print("❌ Нет складов")
        elif not self.sales_points:
            print("❌ Нет пунктов продаж")
        else:
            storage = self.storages[0]
            products = storage.get_all_products()
            
            if not products:
                print("📭 На складе нет товаров. Сначала купите товары (пункт 5)")
            else:
                print("Товары на складе:")

                for i, p in enumerate(products):
                    print(f"  {i+1}. {p}")
                
                try:
                    prod_idx = int(input("Какой товар? ")) - 1
                    
                    if prod_idx < len(products):
                        product = products[prod_idx]
                        
                        print("Пункты продаж:")

                        for i, sp in enumerate(self.sales_points):
                            print(f"  {i+1}. {sp.get_id()} - {sp.get_address()}")
                        
                        sp_idx = int(input("В какой пункт? ")) - 1
                        
                        if sp_idx < len(self.sales_points):
                            sales_point = self.sales_points[sp_idx]
                            transfer_done = False
                            
                            for cell in storage.get_cells():
                                for prod in cell.get_products():
                                    if prod.get_id() == product.get_id() and transfer_done is False:
                                        cell.delete_product(product)
                                        
                                        for sp_cell in sales_point.get_cells():
                                            if sp_cell.add_product(product) and transfer_done is False:
                                                print(f"✅ Товар перемещен в {sales_point.get_id()}")
                                                transfer_done = True
                                        
                                        if transfer_done is False:
                                            cell.add_product(product)
                                            print("❌ Нет места в пункте продаж")
                                            transfer_done = True
                        else:
                            print("❌ Неверный номер пункта")
                    else:
                        print("❌ Неверный номер товара")
                except:
                    print("❌ Ошибка")
        
        return result

    def sell_product(self) -> None:
        """Продажа товара."""
        
        result = None

        if not self.sales_points:
            print("❌ Нет пунктов продаж")
        else:
            print("Пункты продаж:")

            for i, sp in enumerate(self.sales_points):
                print(f"  {i+1}. {sp.get_id()}")
            
            try:
                sp_idx = int(input("Выберите пункт: ")) - 1
                
                if sp_idx < len(self.sales_points):
                    sales_point = self.sales_points[sp_idx]
                    products = sales_point.get_all_products()

                    if not products:
                        print("📭 Нет товаров в пункте продаж. Сначала переместите товары со склада (пункт 2)")
                    else:
                        print("Товары:")

                        for i, p in enumerate(products):
                            print(f"  {i+1}. {p}")
                        
                        prod_idx = int(input("Какой товар? ")) - 1
                        
                        if prod_idx < len(products):
                            product = products[prod_idx]

                            name = input("Имя покупателя: ")
                            phone = input("Телефон: ")

                            customer = Customer(name, phone)
                            self.customers.append(customer)

                            order = self.sales_ops.sell_product(sales_point, product, customer, self.company)

                            if order:
                                self.orders.append({
                                    "id": order.get_id(),
                                    "customer": name,
                                    "total": order.get_total_cost(),
                                    "status": "completed"
                                })
                                self.save_data()
                                print(f"💰 Баланс компании: {self.company.net_worth:.2f} руб.")
                        else:
                            print("❌ Неверный номер товара")
                else:
                    print("❌ Неверный номер пункта")
            except:
                print("❌ Ошибка")
        
        return result

    def show_available_products(self) -> None:
        """Товары доступные к закупке."""
        
        if not self.catalog:
            print("❌ Каталог не загружен")
        else:
            print("\n📋 ТОВАРЫ ДОСТУПНЫЕ К ЗАКУПКЕ (пункт 5 для покупки):")
            for product in self.catalog[:20]:
                print(f"  [{product['id']}] {product['название']} - {product['цена']} руб. (объем: {product['объём']})")

    def storage_products(self) -> None:
        """Товары на складе."""
        
        if not self.storages:
            print("Нет складов")
        else:
            products = self.storages[0].get_all_products()
            
            if not products:
                print("📭 На складе нет товаров. Купите товары (пункт 5)")
            else:
                self.info_ops.get_products_info(self.storages[0])
    
    def return_product(self) -> None:
        """Возврат товара."""
        
        if not self.orders:
            print("❌ Нет заказов")
        else:
            print("\n📋 ЗАКАЗЫ:")
            
            recent_orders = self.orders[-5:] if len(self.orders) > 5 else self.orders
            
            for o in recent_orders:
                status_symbol = "✅" if o["status"] == "completed" else "🔄"

                print(f"  {status_symbol} #{o['id']:.0f} | {o['customer']} | {o['total']} руб.")
            
            try:
                order_id = float(input("\nНомер заказа для возврата: "))
                found_order = None
                
                for o in self.orders:
                    if o["id"] == order_id and found_order is None:
                        found_order = o
                
                if found_order is None:
                    print("❌ Заказ не найден")
                elif found_order["status"] != "completed":
                    print("❌ Товар уже возвращен")
                else:
                    confirm = input(f"Вернуть заказ на {found_order['total']} руб.? (да/нет): ")
                    
                    if confirm == "да":
                        self.company.net_worth -= found_order["total"]
                        found_order["status"] = "returned"

                        self.save_data()

                        print("✅ Возврат оформлен")
                    else:
                        print("❌ Возврат отменен")
            except:
                print("❌ Ошибка")
    
    def buy_products_ui(self) -> None:
        """Закупка товара."""
    
        if self.catalog:
            run_purchase_ui(self.company, self.storages[0]) 
        else:
            print("❌ Каталог не загружен. Запустите product_generator.py")
    
    def hire_employee(self) -> None:
        """Найм сотрудника."""

        position = input("Должность сотрудника: ")

        employee = Employee(position)

        self.employees.append(employee)

        print(f"✅ Сотрудник нанят (ID: {employee.id})")
    
    def fire_employee(self) -> None:
        """Увольнение сотрудника."""

        if self.employees:
            print("Сотрудники:")

            for i, e in enumerate(self.employees):
                print(f"  {i+1}. ID:{e.id} - {e.position}")
            
            try:
                idx = int(input("Кого уволить? ")) - 1
                fired = self.employees.pop(idx)

                print(f"Сотрудник {fired.id} уволен")
            except:
                print("Ошибка")
        else:
            print("Нет сотрудников")
    
    def change_header(self) -> None:
        """Смена ответственного лица."""

        new_header = input("Новое ответственное лицо: ")

        self.company.set_header(new_header)

        print(f"✅ Ответственное лицо: {self.company.get_header()}")
    
    def open_storage(self) -> None:
        """Открытие склада."""

        self.storage_ops.open_storage(self.storages)
    
    def close_storage(self) -> None:
        """Закрытие склада."""

        if len(self.storages) > 1:
            print("Склады:")
            for i, s in enumerate(self.storages):
                print(f"  {i+1}. {s.get_id()}")
            
            try:
                idx = int(input("Какой закрыть? ")) - 1

                self.storage_ops.close_storage(self.storages[idx], self.storages)
            except:
                print("Ошибка")
        else:
            print("❌ Нельзя закрыть единственный склад")
    
    def open_sales_point(self) -> None:
        """Открытие пункта продаж."""

        address = input("Адрес пункта продаж: ")

        self.storage_ops.open_sales_point(self.sales_points, address)
    
    def close_sales_point(self) -> None:
        """Закрытие пункта продаж."""

        if self.sales_points:
            print("Пункты продаж:")
            for i, sp in enumerate(self.sales_points):
                print(f"  {i+1}. {sp.get_id()}")
            
            try:
                idx = int(input("Какой закрыть? ")) - 1

                self.storage_ops.close_sales_point(self.sales_points[idx], self.sales_points)
            except:
                print("Ошибка")
        else:
            print("Нет пунктов продаж")
    
    def storage_info(self) -> None:
        """Информация о складе."""

        if self.storages:
            for storage in self.storages:
                self.info_ops.get_storage_info(storage)
        else:
            print("Нет складов")
    
    def sales_point_info(self) -> None:
        """Информация о пункте продаж."""

        if self.sales_points:
            for sp in self.sales_points:
                self.info_ops.get_sales_point_info(sp)
        else:
            print("Нет пунктов продаж")
    
    def storage_products(self) -> None:
        """Товары на складе."""

        if self.storages:
            self.info_ops.get_products_info(self.storages[0])
        else:
            print("Нет складов")
    
    def sales_point_products(self) -> None:
        """Товары на пункте продаж."""

        if self.sales_points:
            print("Выберите пункт продаж:")

            for i, sp in enumerate(self.sales_points):
                print(f"  {i+1}. {sp.get_id()}")

            try:
                idx = int(input("Номер: ")) - 1

                self.info_ops.get_products_info(self.sales_points[idx])
            except:
                print("Ошибка")
        else:
            print("Нет пунктов продаж")
    
    def show_available_products(self) -> None:
        """Товары доступные к закупке."""

        if self.catalog:
            print("\n📋 ТОВАРЫ ДОСТУПНЫЕ К ЗАКУПКЕ:")
            for product in self.catalog[:20]:
                print(f"  {product['название']} - {product['цена']} руб.")
        else:
            print("❌ Каталог не загружен")

    def company_profit(self) -> None:
        """Доходность предприятия"""

        self.info_ops.get_company_profit(self.company, self.sales_points)
    
    def save_and_exit(self) -> None:
        self.save_data()
        
        print("👋 До свидания!")


if __name__ == "__main__":
    crm = CRM()
    crm.run()
    