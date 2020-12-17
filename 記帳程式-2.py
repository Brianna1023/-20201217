#可以產生記帳程式的文件
product = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = [name, price]
	product.append(p)
#寫入文件，且含有標題(注意編碼)
with open('product.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品' + ',' + '價格' + '\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')
