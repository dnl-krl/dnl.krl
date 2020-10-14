# 1.
value = input('Введите число меньше 100:')
value = int(value)

new_value = value / 2 if value < 100 else -value
print(new_value)

####################################################

# 2.
value = input('Введите число меньше 100:')
value = int(value)

new_value = 1 if value < 100 else 0
print(new_value)

####################################################

# 3.
value = input('Введите число меньше 100:')
value = int(value)

new_value = bool(1) if value < 100 else bool(0)
print(new_value)

####################################################

# 4.
my_str = input('Введите слово:')
print(my_str.upper())

####################################################

# 5.
my_str = input('Введите ФИО:')
print(my_str.lower())

####################################################

# 6.
my_str = input('Введите слово:')
new_str = len(my_str)
result = my_str + my_str if new_str < 5 else my_str
print(result)

####################################################

# 7.
my_str = input('Введите слов:')
len_str = len(my_str)
rev_str = my_str[::-1]

result = my_str + rev_str if len_str < 5 else my_str
print(result)

####################################################

# 8.
my_str = input('Введите, что хотите:')

for i in my_str:
    if i.isalnum():
        print(i)

####################################################

# 9.
my_str = input('Введите, что хотите:')

for i in my_str:
    if not i.isalnum():
        print(i)

####################################################

# 10.
my_str = input('Введите, что хотите:')

for i in my_str:
    if not (i.isalnum() or i.isspace()):
        print(i)
