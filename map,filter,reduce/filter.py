# filter function aik aesi list banata ha elements ki jis pr given function
# true return karta ha

list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5, list_1))
#filter function ka syntax filter(function, list(iterable))
print(gr_than_5)