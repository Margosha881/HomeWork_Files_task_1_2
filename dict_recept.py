with open('recept.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingr_count = int(file.readline())
        menu = []
        for _ in range(ingr_count):
            list = file.readline().strip().split(' | ')
            ingridiens_name, quantity, mearsure = list
            menu.append({'ingridiens_name': ingridiens_name,
                         'quantity': int(quantity), 'mearsure': mearsure})
        file.readline()
        cook_book[dish] = menu

import json
print(f'cook_book= {json.dumps(cook_book, ensure_ascii=False, indent=4)}')


def get_shop_list_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            item = dict(ingridient)
            item['quantity'] *= person_count
            if item['ingridiens_name'] not in shop_list:
                shop_list[item['ingridiens_name']] = item
            else:
                shop_list[item['ingridiens_name']]['quantity'] += item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print({shop_list_item['ingridiens_name']}, {shop_list_item['quantity']}, {shop_list_item['mearsure']})


def create_shop_list():
    person_count = int(input('Укажите количество человек: '))
    dishes = input('Укажите название блюда (через запятую): ').title().split(', ')
    shop_list = get_shop_list_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()


