import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'files/recipes.txt')

with open(file_path, encoding = 'utf-8') as file:
    cook_book = {}

    for book in file:
        dish_name = book.strip()
        amount_of_ingridients = int(file.readline().strip())
        for item in range(amount_of_ingridients):
            list = ingridient, quantity, measure = file.readline().split('|')
            cook_book[dish_name] = list
        file.readline()
    pprint(cook_book)

    def get_shop_list_by_dishes(dishes, person_count, cook_book):
        shop_list = {}

        for dish in dishes:
            if dish in cook_book:
                for ingridient in cook_book[dish]:
                    new_shop_list_item = dict(ingridient)
                    new_shop_list_item['quantity'] *= person_count
                    if new_shop_list_item['ingridient_name'] not in shop_list:
                        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
                    else:
                        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
        return shop_list


    pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Омлет', 'Запеченный картофель', 'Фахитос'], 1, cook_book))