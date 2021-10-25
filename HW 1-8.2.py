import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'recipes.txt')

with open(file_path, encoding = 'utf-8') as file:

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        same_dishes_count_dict = {dish: dishes.count(dish) for dish in dishes} ## Считаем количество "омлетов" через создание словаря
        print(same_dishes_count_dict)

        for book in file:
            dish_name = book.strip() ## получаем название блюда

            if dish_name in same_dishes_count_dict.keys():  ## если название блюда в новом словаре с омлетами
                dish_name_count = same_dishes_count_dict.get(dish_name)  ## Получаем счетчик таких блюд
                amount_of_ingridients = int(file.readline().strip())  ## counting the lines to go for a dish

                for item in range(amount_of_ingridients):
                    ingridient, quantity, measure = file.readline().split('|')  # получили список ингридиента через , убрав |
                    quantity = int(quantity)
                    if ingridient in shop_list.keys():  # если такой ингридиет уже есть в словаре тогда
                        current_ingridietnt_quantity = shop_list[ingridient].get('quantity')
                        shop_list[ingridient] = {'quantity': quantity + current_ingridietnt_quantity}
                    else:
                        shop_list[ingridient] = {'measure': measure.strip(), 'quantity': quantity * person_count * dish_name_count}
                file.readline()  ## заглушаем пустую строку до следующего блюда
            else:
                amount_of_lines_to_pass = int(file.readline().strip()) ## гоним до следующего блюда
                for line in range(amount_of_lines_to_pass):
                    file.readline()
                file.readline()

        return shop_list

    # pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински', 'Фахитос'], 2))
    pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Омлет', 'Запеченный картофель', 'Фахитос'], 1))