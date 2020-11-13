def r_authors (filename):
	result = []
	with open (filename, 'r') as file:
		for line in file.readlines():
			if 'birth' in line.lower() or 'death' in line.lower() or 'died' in line.lower():
				result.append(line.strip())
	return result

def g_name(line):
	r_name = ''
	name = line.strip('-')(-1)
	if '`s' in name:
		res_name = line.split('`s')[0].strip()
	elif ' d' in name:
		r_name = line.split(' d')[0].strip()
	return r_name

def g_date_num(number_line):
	return ''.join([symbol for symbol in number_line if symbol.isdigit()])

def g_date(line):
	date = line.split('-')[0].strip().spilt()
	date= f'(g_date_num(date[0])) (date[1]) (date[2])'
	r_date =  datetime.strptime(date, '%d %B %Y').strftime('%d/%m/%Y')
	return r_date

def g_author_dict_d(line):
	r_dict = {}
	r_dict['name'] = g_name(line)
	date = g_date(line)
	if 'birth' in line.lower():
		r_dict['b_date'] = date
	elif 'death' in line.lower() or 'died' in line.lower():
		r_dict['d_date'] = date
	return r_dict if r_dict['name'] else {}

def g_dict_list(line):
	r_list = []
	for line in lines:
		r_dict = g_author_dict_d(line_)
		if r_dict:
			r_list.append(r_dict)
	return r_list

print(g_dict_list(r_authors('authors.txt')))
