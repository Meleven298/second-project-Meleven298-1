import csv
import json
import random


products_data = {
    "еда": ["Молоко", "Хлеб", "Сок", "Йогурт", "Сыр", "Масло", "Колбаса", "Печенье", "Чай", "Кофе", "Рис", "Макароны", "Конфеты", "Мороженое", "Яйца"],
    "техника": ["Телефон", "Ноутбук", "Планшет", "Наушники", "Колонка", "Телевизор", "Микроволновка", "Холодильник", "Пылесос", "Утюг", "Фен", "Блендер", "Кофеварка", "Робот-пылесос", "Электрочайник"],
    "одежда": ["Футболка", "Джинсы", "Куртка", "Шапка", "Кроссовки", "Ботинки", "Платье", "Пиджак", "Свитер", "Шорты", "Носки", "Перчатки", "Шарф", "Ремень", "Рубашка"],
    "мебель": ["Стул", "Стол", "Диван", "Кровать", "Шкаф", "Комод", "Кресло", "Тумба", "Стеллаж", "Полка", "Пуф", "Кухонный гарнитур", "Барный стул", "Трюмо", "Вешалка"],
    "инструменты": ["Дрель", "Шуруповёрт", "Молоток", "Отвёртка", "Пила", "Рубанок", "Гаечный ключ", "Пассатижи", "Уровень", "Рулетка", "Ножовка", "Тиски", "Набор свёрл", "Угольник", "Наждачная бумага"]
}

adjectives = ["профессиональный", "домашний", "современный", "удобный", "мощный", "компактный", "стильный", "классический", "премиум", "эконом", "надёжный", "лёгкий"]

modifiers_by_category = {
    "еда": ["свежий", "натуральный", "органический", "без ГМО", "домашний", "фермерский", "охлаждённый"],
    "техника": ["с Bluetooth", "Wi-Fi управление", "сенсорный", "бесшумный", "энергосберегающий", "нового поколения", "с приложением"],
    "одежда": ["дышащий", "водоотталкивающий", "утеплённый", "повседневный", "спортивный", "эластичный", "из хлопка"],
    "мебель": ["складной", "трансформируемый", "мягкий", "деревянный", "металлический", "лаконичный", "эргономичный"],
    "инструменты": ["аккумуляторный", "сетевой", "ударный", "точный", "прочный", "портативный", "с подсветкой"]
}


def generate_product(product_id: int) -> dict:
    '''Сгенерировать продукты.
    
    Args: 
        product_id: Айди продукта.
        
    Returns:
        Словарь содержащий информацию о продукте.
    '''

    category = random.choice(list(products_data.keys()))

    base_name = random.choice(products_data[category])

    if random.random() < 0.7:
        adj = random.choice(adjectives)
        name = f"{adj} {base_name}"
    else:
        name = base_name

    if random.random() < 0.4:
        mod = random.choice(modifiers_by_category[category])
        name = f"{name} ({mod})"

    if category == "техника":
        price = round(random.randint(1000, 150000), 2)

        volume = random.randint(2, 20)
    elif category == "мебель":
        price = round(random.randint(1000, 80000), 2)

        volume = random.randint(3, 30)
    elif category == "одежда":
        price = round(random.randint(500, 30000), 2)

        volume = random.randint(1, 3)
    elif category == "инструменты":
        price = round(random.randint(200, 50000), 2)

        volume = random.randint(2, 20)
    else:
        price = round(random.randint(50, 5000), 2)

        volume = random.randint(1, 2)
    
    return {
        "id": product_id,
        "название": name,
        "категория": category,
        "цена": price,
        "объём": volume
    }


products = [generate_product(i + 1) for i in range(100)]

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

with open("products.csv", "w", encoding="utf-8", newline="") as csvfile:
    fieldnames = ["id", "название", "категория", "цена", "объём"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(products)

category_counts = {}

for product in products:
    cat = product["категория"]
    category_counts[cat] = category_counts.get(cat, 0) + 1
