# 1.

my_int = 10010001101001100001
my_int = str(my_int)
symbol = '0'

count = my_int.count(symbol)
print(count)

# 2.

my_int = 110000110001110001110000
symbol = 0

for i in str(my_int)[::-1]:
    if i == '0':
        symbol += 1
    else:
        break

print(symbol)

# 3.

my_list_1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
my_list_2 = [55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

my_result_1 = []
my_result_2 = []

for symb in my_list_1:
    if symb % 2 == 0:
        my_result_1.append(symb)
    else:
        my_result_2.append(symb)
my_result = my_result_1 + my_result_2
print(my_result)

# 4.

my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
first_element = my_list.pop(0)
new_list = my_list.copy()
new_list.append(first_element)

print(new_list)

# 5.

my_list = [55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
first_element = my_list.pop(0)
my_list.append(x)
print(my_list)

# 6.

my_str = "43 больше чем 34 но меньше чем 56"
number = my_str.split(' ')
product = 0
for i in number:
    try:
        value = int(i)
        product += value
    except:
        pass
print(product)
