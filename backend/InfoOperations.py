class InfoOperations:
    '''Класс операций над информацией.'''
    
    @staticmethod
    def get_storage_info(storage) -> None:
        """Информация о складе.
        
        Args:
            storage: Склад.
        """

        print(f"\n📦 Склад: {storage.get_id()}")
        print(f"📊 Всего ячеек: {len(storage.get_cells())}")
        print(f"📦 Общий занятый объем: {storage.get_total_volume()}/1000")
        print(f"🗂️ Товаров на складе: {len(storage.get_all_products())}")
    
    @staticmethod
    def get_sales_point_info(sales_point) -> None:
        """Информация о пункте продаж.
        
        Args:
            sales_point: Пункт продаж.
        """

        status = "🟢 Работает" if sales_point.is_open() else "🔴 Закрыт"

        print(f"\n🏪 Пункт продаж: {sales_point.get_id()}")
        print(f"📍 Адрес: {sales_point.get_address()}")
        print(f"📊 Статус: {status}")
        print(f"💰 Выручка: {sales_point.get_revenue():.2f} руб.")
    
    @staticmethod
    def get_products_info(storage_or_point) -> None:
        """Товары на складе/пункте.

        Args:
            storage_or_point: Это склад или пункт продажи.
        """

        products = storage_or_point.get_all_products()

        if not products:
            print("📭 Товаров нет")
        else:
            print(f"\n📋 Список товаров:")

            for i, product in enumerate(products, 1):
                print(f"  {i}. {product}")
    
    @staticmethod
    def get_company_profit(company, sales_points) -> None:
        """Доходность предприятия.
        
        Args:
            company: Компания.
            sales_points: Пункт продаж.
        """

        total_revenue = sum(sp.get_revenue() for sp in sales_points)

        print(f"\n💰 ФИНАНСОВЫЙ ОТЧЕТ 💰")
        print(f"📊 Баланс компании: {company.net_worth:.2f} руб.")
        print(f"📊 Общая выручка с пунктов продаж: {total_revenue:.2f} руб.")
        print(f"📊 Итоговая прибыль: {company.net_worth:.2f} руб.")
