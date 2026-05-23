from backend.classes.Company import Company
from backend.classes.Storage import Storage
from backend.ProductOperations import load_catalog, buy_products

import os
import sys
from typing import List, Dict


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def show_catalog(catalog: List[Dict]) -> None:
    """Показывает каталог."""

    print("\n" + "="*80)
    print(" КАТАЛОГ ТОВАРОВ")
    print("="*80)
    
    categories = {}

    for product in catalog:
        cat = product["категория"]

        if cat not in categories:
            categories[cat] = []

        categories[cat].append(product)
    
    for category, products in categories.items():
        print(f"\n{category.upper()}:")
        print("-"*60)

        for product in products:
            print(f"  [{product['id']:3d}] {product['название']:<40} | {product['цена']:8.2f} руб.")


def run_purchase_ui(company: Company, storage: Storage) -> None:
    """Фронтенд для закупки."""

    catalog = load_catalog("products.json")
    
    if not catalog:
        print("Каталог не загружен! Запустите product_generator.py")
    else:
        cart = []
        menu_active = True
        
        while menu_active:
            print("\n" + "="*60)
            print("МЕНЮ ЗАКУПКИ")
            print("="*60)
            print("1. Показать каталог")
            print("2. Добавить товар в корзину")
            print("3. Оформить закупку")
            print("4. Показать корзину")
            print("5. Показать баланс")
            print("6. Выйти")
            
            choice = input("\nВыберите действие: ").strip()
            
            if choice == "1":
                show_catalog(catalog)
            
            elif choice == "2":
                try:
                    product_id = int(input("ID товара: "))
                    product_data = None
                    
                    for p in catalog:
                        if p["id"] == product_id:
                            product_data = p
                    
                    if product_data is not None:
                        quantity = int(input("Количество: "))
                        
                        if quantity > 0:
                            cart.append((product_data, quantity))
                            print(f"Добавлено: {product_data['название']} x{quantity}")
                        else:
                            print("Количество должно быть > 0")
                    else:
                        print("Товар не найден")
                    
                except ValueError:
                    print("Введите число")
            
            elif choice == "3":
                if len(cart) > 0:
                    print(f"\nБаланс компании: {company.net_worth:.2f} руб.")
                    print("Товары в корзине:")
                    
                    for product_data, quantity in cart:
                        print(f"  - {product_data['название']} x{quantity} = {product_data['цена'] * quantity:.2f} руб.")
                    
                    confirm = input("\nПодтвердить закупку? (да/нет): ").strip().lower()
                    
                    if confirm == "да":
                        success, total_cost, message = buy_products(storage, company, cart)
                        
                        if success:
                            print(f"{message}")
                            print(f"Списано: {total_cost:.2f} руб.")
                            print(f"Новый баланс: {company.net_worth:.2f} руб.")
                            cart.clear()
                        else:
                            print(f"{message}")
                    else:
                        print("Закупка отменена")
                else:
                    print("Корзина пуста")
            
            elif choice == "4":
                if len(cart) > 0:
                    print("\nКОРЗИНА:")
                    
                    total = 0
                    
                    for product_data, quantity in cart:
                        item_total = product_data["цена"] * quantity
                        total += item_total
                        print(f"  {product_data['название']} x{quantity} = {item_total:.2f} руб.")
                    
                    print(f"  ИТОГО: {total:.2f} руб.")
                else:
                    print("Корзина пуста")
            
            elif choice == "5":
                print(f"\nБаланс компании: {company.net_worth:.2f} руб.")
            
            elif choice == "6":
                print("Возврат в главное меню")
                menu_active = False
            
            else:
                print("Неверный выбор")
