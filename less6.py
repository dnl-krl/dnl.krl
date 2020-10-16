# 1.
my_list = ['qwe', 'rty', 'uio']
new_list = []
for index, value in enumerate(my_list):
    if index % 2 == 1:
        value = value[::-1]
        new_list.append(value)
    else:
        value = value
        new_list.append(value)
print(new_list)

################################################################

# 2.
my_list = ['anna', 'lisa', 'adele', 'nina']
a = 'a'
new_list = []

for i in my_list:
    if i[0] == a:
        new_list.append(i)
print(new_list)

################################################################

# 3.
my_list = ['anna', 'friend', 'adele', 'ted', 'a', 'qwerty']
a = 'a'
new_list = []

for i in my_list:
    if not i.find(a):
        new_list.append(i)
print(new_list)

################################################################

# 4.
my_list = [123, 'qwe', 456, 'rty', 789, 'uio']
new_list = []

for value in my_list:
    if type(value) == str:
        new_list.append(value)
print(new_list)

################################################################

# 5.
my_str = 'avada kedavra'
my_str = set(my_str)
print(list(my_str))

################################################################

# 6.
my_str_1 = 'qwertyqw'
my_str_2 = 'qweuio'

new_list = []

for i in my_str_1 and my_str_2:
    if my_str_1.find(i) == my_str_2.find(i):
        new_list.append(i)
print(new_list)

################################################################

# 7.
my_str_1 = 'qwertyqw'
my_str_2 = 'qweuio'

new_list = []

for i in my_str_1 and my_str_2:
    if my_str_1.find(i) == my_str_2.find(i):
        new_list.append(i)
print(new_list)

################################################################

# 8.
human = {'Фамилия': 'Курило',
         'Имя': 'Даниил',
         'Возраст': 25,
         'Адрес проживания': ('Украина', 'Днепр', 'Семафорная'),
         'Работа': ('Работает', 'PPC-специалист')}

print(human)

################################################################

# 9.
cakes = {'Мука': '500 гр',
        'Молоко': '100 мл',
        'Масло': '100 гр',
        'Яйцо': '10 шт'}

cream = {'Сахар': '100 гр',
         'Масло': '100 гр',
         'Ваниль': '10 гр',
         'Сметана': '150 гр'}

glaze = {'Какао': '100 гр',
         'Сахар': '100 гр',
         'Масло': '50 гр'}

recipe = {'Коржи': cakes,
          'Крем': cream,
          'Глазурь': glaze}

print(recipe)
