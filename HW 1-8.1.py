import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'recipes.txt')

with open(file_path, encoding = 'utf-8') as file:
    cook_book = {}
    for book in file:
        dish_name = book.strip()
        amount_of_ingridients = int(file.readline().strip())
        temp_data = []
        for item in range(amount_of_ingridients):
            ingridient, quantity, measure = file.readline().split('|')
            ingridient_line = {'ingridiet_name': ingridient.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()}
            temp_data.append(ingridient_line)
        cook_book[dish_name] = temp_data
        file.readline().strip()
    pprint(cook_book)