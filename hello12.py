# coding: UTF-8
# 辞書　key value
sales = {"taniguchi":200, "fukoji":300, "dotinstall":500}
print(sales)

print(sales["taniguchi"])
sales["fukoji"] = 800
print(sales)

# in
print("taniguchi" in sales)	#True

# keys, values, items
print(sales.keys())
print(sales.values())
print(sales.items())
print(len(sales))

