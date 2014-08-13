# coding: UTF-8
# for ループ
sales = [13, 23, 31, 238]
sum = 0
for sale in sales:
	sum += sale
	print(sum)
print(sum)

sum = 0
for i in range(10):
	print(i)
	sum = sum + i
else:
	print(sum)

# continue 
sum = 0
for i in range(10):
	if i == 3:
		continue
	print(i)
	sum = sum + i
else:
	print(sum)

# break
sum = 0
for i in range(10):
	if i == 3:
		break
	print(i)
	sum = sum + i
else:
	print(sum)

	
