#產生記帳結果，大清單中裝小清單，只印某個清單，或單獨印價格、價格
product = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = [name, price]
	product.append(p)
print(product)
print(product[0])
print(product[0][0])
print(product[0][1])
for p in product:
	print(p)
	print(p[0])
	print(p[0], '的價格是', p[1])
	