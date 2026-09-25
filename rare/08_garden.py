# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# # В саду сорвали цветы
# garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# # На лугу сорвали цветы
# meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# # Создайте множество цветов, произрастающих в саду и на лугу
# # garden_set =
# # meadow_set =

# garden_set = set(garden)
# meadow_set = set(meadow)

# # Выведите на консоль все виды цветов

# all_flowers = garden_set | meadow_set
# print("Все виды цветов:", all_flowers)

# # Выведите на консоль те, которые растут и там и там

# both_places = garden_set & meadow_set
# print("Цветы, которые растут и в саду, и на лугу:", both_places)

# # Выведите на консоль те, которые растут в саду, но не растут на лугу

# only_garden = garden_set - meadow_set
# print("Цветы, которые растут только в саду:", only_garden)

# # Выведите на консоль те, которые растут на лугу, но не растут в саду

# only_meadow = meadow_set - garden_set
# print("Цветы, которые растут только на лугу:", only_meadow)

def run():
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

    garden_set = set(garden)
    meadow_set = set(meadow)

    print("Все виды цветов:", garden_set | meadow_set)
    print("Цветы, которые растут и в саду, и на лугу:", garden_set & meadow_set)
    print("Цветы, которые растут только в саду:", garden_set - meadow_set)
    print("Цветы, которые растут только на лугу:", meadow_set - garden_set)

if __name__ == '__main__':
    run()