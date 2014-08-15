# coding:UTF-8
# クラスの継承
# オブジェクト（変数と関数をまとめたもの）
# クラス
# インスタンス
class User(object):
	def __init__(self, name):
		self.name = name
	def greet(self):
		print("my name is %s!" % self.name)


class SuperUser(User):			#Userクラスを継承
	def shout(self):		#追加の関数
		print("%s is SUPER" %self.name)

bob = User("Bob")
tom = SuperUser("Tom")
bob.greet()
tom.greet()
tom.shout()


