import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'PycharmProjects/pythonProject/files/recipes.txt')

with open(file_path, encoding = 'utf-8') as file:

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        same_dishes_count_dict = {dish: dishes.count(dish) for dish in dishes}

        for book in file:
            dish_name = book.strip()

            if dish_name in same_dishes_count_dict.keys():
                dish_name_count = same_dishes_count_dict.get(dish_name)
                amount_of_ingridients = int(file.readline().strip())

                for item in range(amount_of_ingridients):
                    ingridient, quantity, measure = file.readline().split('|')
                    quantity = int(quantity)
                    if ingridient in shop_list.keys():
                        current_ingridietnt_quantity = shop_list[ingridient].get('quantity')
                        shop_list[ingridient] = {'quantity': quantity + current_ingridietnt_quantity}
                    else:
                        shop_list[ingridient] = {'measure': measure.strip(), 'quantity': quantity * person_count * dish_name_count}
                file.readline()
            else:
                amount_of_lines_to_pass = int(file.readline().strip())
                for line in range(amount_of_lines_to_pass):
                    file.readline()
                file.readline()

        return shop_list

    pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Омлет', 'Запеченный картофель', 'Фахитос'], 1))