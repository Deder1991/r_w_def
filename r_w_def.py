import os

def read_file(filename):	#讀取檔案
	products = []
	with open(filename, 'r', encoding='utf-8') as file:
		for line in file:
			if '商品名稱,價錢' in line:
				continue
			products.append(line.strip().split(','))
	return products

def input_products():	#輸入商品
	while True:
		name = input('輸入商品名稱:')
		if name == 'q':
			break
		price = input('輸入價格:')
		products.append([name, price])
	return products

def write_file(filename):	#寫入檔案
	with open(filename, 'w', encoding='utf-8') as file:
		file.write('商品名稱,價錢\n')
		for line in products:
			file.write(line[0] + ',' + line[1] + '\n')


	
if os.path.isfile('products.csv'):
	print('有檔案')
	products = read_file('products.csv')
else:
	print('沒檔案')
		
products = input_products()
print(products)
write_file('products.csv')

