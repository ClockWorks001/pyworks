# coding: UTF-8
# リスト＜＞関数　map
def double(x):
	return x * x

print(list(map(double, [2, 5, 8])))

# 無名関数 lambda
print(list(map(lambda x:x * 2, [2, 5, 8])))


