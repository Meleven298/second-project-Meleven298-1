from backend.classes.Storage import Storage
from backend.classes.SalesPoint import SalesPoint

class StorageOperations:
    '''Класс операций над складом.'''
    
    @staticmethod
    def open_storage(storages: list) -> Storage:
        """Открытие нового склада.
        Args:
            storage: Склад.

        Returns:
            new_storage: Новый склад.
        """

        new_id = len(storages) + 1
        new_storage = Storage(new_id)
        storages.append(new_storage)

        print(f"✅ Склад {new_storage.get_id()} успешно открыт!")

        return new_storage
    
    @staticmethod
    def close_storage(storage: Storage, storages: list) -> bool:
        """Закрытие склада.
        
        Args:
            storage: Склад.
            storages: Список складов.
        
        Returns:
            True, если склад успешно закрыт.
        """

        if storage in storages:
            storages.remove(storage)

            print(f"❌ Склад {storage.get_id()} закрыт")

            return True
        
        print("Склад не найден")
    
    @staticmethod
    def open_sales_point(sales_points: list, address: str) -> SalesPoint:
        """Открытие пункта продаж.
        
        Args:
            sales_points: Список точки продаж.
            address: Адресс новой точки продаж.

        Returns:
            new_point: Новая точка продаж.
        """

        new_id = len(sales_points) + 1
        new_point = SalesPoint(new_id, address)
        sales_points.append(new_point)

        print(f"✅ Пункт продаж {new_point.get_id()} по адресу {address} открыт!")

        return new_point
    
    @staticmethod
    def close_sales_point(sales_point: SalesPoint, sales_points: list) -> bool:
        """Закрытие пункта продаж.
        
        Args:
            sales_points: Список точки продаж.
            address: Адресс новой точки продаж.

        Returns:
            True, если точка продаж успешно закрыта.
        """

        if sales_point in sales_points:
            sales_points.remove(sales_point)

            print(f"❌ Пункт продаж {sales_point.get_id()} закрыт")

            return True
        
        print("Пункт продаж не найден")
    