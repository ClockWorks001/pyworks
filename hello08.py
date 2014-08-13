# coding: UTF-8
# リスト
sales = [255, 100, 353, 400]

#len + * []
print( len(sales) ) 	#4
print( sales[2]	)	#353
sales[2] = 100
print( sales[2] )	#100
print( sales )

# in 存在チェック
print( 100 in sales ) 	#True

# 数字の連番を作成する。
# range
r1 = list(range(10))	#リスト型への変換が必要。rangeはリストを返さない。
r2 = range(3,10)	#range(3,10)
print(r1)
print(r2)
print( range(10) )		#range(10)
print( list(range(3,10)) )	#3～9
