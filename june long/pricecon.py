
# cook your dish here
def pricecon(testcases):
	result_array = []
	for i in range(testcases):
		sum = 0
		number_of_items_and_prices = list(map(int,input().split()))
		no_of_items, max_price = number_of_items_and_prices[0],number_of_items_and_prices[1]
		item_price = list(map(int,input().split()))
		for j in range(len(item_price)):
			if item_price[j]>max_price:
				sum = sum + abs(item_price[j]-max_price)
			
		result_array.append(sum)
	return(result_array)



testcases = int(input())
t = pricecon(testcases)
for i in range(len(t)):
	print(t[i])
