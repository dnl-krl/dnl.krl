import string, random, json

# 1.

def line_txt ():
    result = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(100, 1000))
    print (result)

result = line_txt()

###########################################################

# 2.

def gen_data(min_val, max_val):
    list_key = []
    list_value = []

    for i in range (min_val, max_val):
        list_key.append(''.join(random.choice(string.ascii_letters) for _ in range (5)))

    for a in range (min_val, max_val):
        list_value.append(random.randint(-100,100))

    new_dict = dict(zip(list_key, list_value))
    return [new_dict]

outfile = 'new.json'
data = gen_data(5,20)

with open(outfile, 'w') as json_file:
    json.dump(data, json_file, indent=2)

###########################################################
