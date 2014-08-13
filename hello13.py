# coding: UTF-8
#
a = 10
b = 1.234
c = "taguchi"
print("age: %d" % a)	# %d 整数
print("age: %10d" % a)	# %d 整数
print("age: %010d" % a)	# %d 整数

print("price: %f" % b)		# %f フロート
print("price: %.2f" % b)	# %f フロート

print("name: %s" % c)	# %s 文字列

d = {"fukoji":200, "dotinstall":500}
print("sales: %(fukoji)d" %d)
print("%d and %f" %(a,b))

