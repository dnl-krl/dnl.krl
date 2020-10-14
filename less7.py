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

