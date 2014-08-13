# coding: UTF-8
# タプル　（変更ができないlist）
a = (2, 5, 8)

# len + *  []
print( len(a) )	#3
print( a * 2 )	# 2, 5, 8, 2, 5, 8

# タプル　＜＞　リスト　相互変換
b = list(a)
print(b)
c = tuple(b)
print(c)

