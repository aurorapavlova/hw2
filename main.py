import os.path
import os

def acounting(file:str) -> int:
    return sum(1 for _ in open('1.txt', 'rt', encoding='utf-8'))

cook_book = {}
with open('recipes.txt', 'rt', encoding = 'utf-8') as f:
    for line in f:
        dish = line.strip()
        ingredients_quantity = f.readline()
        ingredients_list = []
        for i in range(int(ingredients_quantity)):
            emp = f.readline()
            name, quantity, measure = emp.strip().split(' | ')
            ingredients_list.append({'ingredient_name': name,
                                     'quantity': quantity,
                                     'measure': measure})

        f.readline()
        cook_book[dish] = ingredients_list
#print(f'cook_book = {cook_book}')

def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] = int(consist['quantity']) * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'], 'quantity': (int(consist['quantity']) * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)

#get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

def rewriting(file_for_writing: str, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        files.append([acounting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
    for file_from_list in sorted(files):
        opening_files = open(file_for_writing, 'a')
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r',encoding='utf-8') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()

file_for_writing = os.path.abspath('C:\Пользователи\pavlo\Python\1.txt')
base_path = os.getcwd()
location = os.path.abspath('C:\Пользователи\pavlo\Python')
rewriting(file_for_writing, base_path, location)



