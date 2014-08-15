# coding: UTF-8
# 変数のスコープ
name = "taguchi"
def hello():
	name = "fkoji"	#これは関数のなかのローカル変数

def hello2():
	pass		#中身のない関数を作るときには"pass"を記載する。

def hello3():
	global name	#グローバル変数を使う場合は、globalで指定する。
	name = "dotinstall"

hello()
print(name)
hello2()
hello3()
print(name)



