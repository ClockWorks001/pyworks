# coding: UTF-8
# 関数
# 引数
def hello(name, num = 3):
	print("hello %s! " %name *num)

hello("Tom", 2)
hello("Steve")			#初期値　3回が適用
hello(num = 4, name = "Bob")	#引数名を指定すれば、順番が変わってもok

# 返り値
def bay(name, num = 3):
	return("bay %s! " %name *num)

s = bay("keit", 2)
print(s)

