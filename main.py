boys_dating = [str(names) for names in input('Введите имена мальчиков через запятую: ').split(', ')]
girls_dating = [str(names) for names in input('Введите имена девочек через запятую: ').split(', ')]

if len(boys_dating)==len(girls_dating):
    print("Идеальные пары: ")
    boys_dating.sort()
    girls_dating.sort()
    sorted_dating = zip(boys_dating, girls_dating)
    for best_date in sorted_dating:
        print(f"{best_date[0].capitalize()} и {best_date[1].capitalize()}")
else:
    print("Кто то может остаться без пары!")

# if len(boys_dating)==len(girls_dating):
#     print("Идеальные пары: ")
#     boys_dating.sort()
#     girls_dating.sort()
#     sorted_dating = zip(boys_dating, girls_dating)
#     for boys, girls in sorted_dating:
#         print(f"{boys.capitalize()} и {girls.capitalize()}")
# else:
#     print("Кто то может остаться без пары!")

person_at_party = int(input('Введите количество гостей: '))

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]

for dish in cook_book:
    print(f'\n{dish[0].title()}:')
    for ingridients in dish[1]:
        print(f'{ingridients[0]}, {ingridients[1] * person_at_party} {ingridients[2]}')