# coding: UTF-8
# 文字列
# len 文字数
# find　検索
# []　切り出し
s = "abcdefghi"	
print len(s)		#9
print s.find("c")	#2
print s.find("x")	#-1
print s[2]		#c
print s[2:5]		#cde
print s[:5]		#abcde
print s[5:]		#fghi
print s[2:-1]		#cdefgh
