import random
from random import randint, choice

# 1.
value = 20
gen_list = [randint(1,100) for _ in range(value)]

print(gen_list)

####################################################

# 2.
gen_cord = random.randint(1, 100)
list_x = [randint(1,100) for _ in range(gen_cord)]
list_y = [randint(1,100) for _ in range(gen_cord)]

cord_a = (choice(list_x), choice(list_y))
cord_b = (choice(list_x), choice(list_y))
cord_c = (choice(list_x), choice(list_y))

my_dict = dict(a = cord_a, b = cord_c, c = cord_b)

print(my_dict)

####################################################

# 3.

def my_print ():
    print('***',my_str,'***')

my_str = 'lesson7'
my_print()

####################################################

# 4.

my_dict_1 = {'a': 1, 'b': 10, 'c': '10', 'd': 'hello', 'f': 16.09, 'e': 'world'}
my_dict_2 = {'b': 10, 'd': 'hello', 'e': 'world', 'f': 16.09}

dict_1 = set(my_dict_1)
dict_2 = set(my_dict_2)

my_res_sym = dict_1.intersection(my_dict_2)
print(list(my_res_sym))

my_res_dif = dict_1.difference(my_dict_2)
print(list(my_res_dif))

new_dict = dict()
for key, value in my_dict_1.items() and my_dict_2.items():
    if key not in my_dict_2:
        new_dict.update(key, value)
        print(new_dict)
    else:
        pass

print(my_dict_1.keys())

