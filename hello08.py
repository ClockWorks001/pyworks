# coding: UTF-8
# ���X�g
sales = [255, 100, 353, 400]

#len + * []
print( len(sales) ) 	#4
print( sales[2]	)	#353
sales[2] = 100
print( sales[2] )	#100
print( sales )

# in ���݃`�F�b�N
print( 100 in sales ) 	#True

# �����̘A�Ԃ��쐬����B
# range
r1 = list(range(10))	#���X�g�^�ւ̕ϊ����K�v�Brange�̓��X�g��Ԃ��Ȃ��B
r2 = range(3,10)	#range(3,10)
print(r1)
print(r2)
print( range(10) )		#range(10)
print( list(range(3,10)) )	#3�`9
