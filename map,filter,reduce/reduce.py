from functools import reduce

list1 = [1,2,3,4,2]
#e.g : ma chata hon 1+2+3+4+2 = 12 yani sum of list1
num = reduce(lambda x,y:x+y, list1)
num1 = reduce(lambda x,y:x*y, list1)
# num = 0
# for i in list1:
#     num = num + i
print(num)
print(num1)