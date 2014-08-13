# coding: UTF-8
# セット（集合型）　－重複をゆるさない
a = set([1, 2, 3, 4, 3, 2])
print(a)
b = {3, 4, 5}
print(a - b)
print(a | b)	#和集合は　｜
print(a & b)	#積集合は　＆　a,bで同じものが返る
print(a ^ b)	#どちらかにしあ存在しないもの

