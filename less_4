# 1.
my_list = [123, 123902, 89, 92, 101, 321, 123, 7, 10]
a = ''
for i in my_list:
    if i > 100:
        print(i)

#######################################################

# 2.
my_list = [123, 123902, 89, 92, 101, 321, 123, 7, 10]
my_result = []

for i in my_list:
    if i > 100:
        my_result.append(i)
print(my_result)

#######################################################

# 3.
my_list = [123, 1, 23, 109]

len_list = len(my_list)
if len_list <= 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)

#######################################################

# 4.
value = input('Введите число:')
try:
    result = float(value) ** -1
except:
    print('Некорректный ввод...')
    result = 0.0
print(result)

#######################################################

# 5.
my_list = [123, 'dude', 101, 'wow', 'how are you?', 16.09]
my_index = [0, 1, 2, 3, 4, 5]

for index in my_index:
    print(my_list[index])

#######################################################

# 6.
my_list_1 = [123, 'dude', 101, 'wow', 'how are you?', 16.09]
my_list_2 = ['101, YouTube!', 'I`m fine!', 26.09, 6, 01.10, 1995]
my_index = [0, 1, 2, 3, 4, 5]

for index in my_index:
    result = my_list_1[index], my_list_2[index]
    print(result)

#######################################################

# 7.
my_str = '0123456789'

my_list = []
for symb_1 in my_str:
    for symb_2 in my_str[::-1]:
        result = symb_1 + symb_2
        result = int(result)
        my_list.append(result)
        my_list.sort()
print(my_list)
