#map function kisi bhi aik function ko  aik pori list ma apply kar deta ha

 

# numbers=["3","34","64"]

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers[2])

#lekin hr time for chalana achi baat nahi ha

#map(first argument function(yani wo fuction jo ap lagana chatahin),second argument numbers (yani kis jga ap lagana chata ha) )
# numbers=list(map(int,numbers)) #int function ko numbers list ma apply kar deta ha
# print(numbers)

def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]
# num = [2,3,5,6,76,3,3,2]
# for i in range(5):
#     val = list(map(lambda x: x(i) , func))
#     # val = list(map(lambda x:f"the square and cube of is{str(i)}"+str(x(i)) , func))
#     print(val)
while True:
    num = input("Enter the number you want the square and cube : ")
    if num == "q":
        break
    else:
        num = int(num)
        val = list(map(lambda x: x(num) , func))
        print(val)
# num=int(input("enter the number yo want to squr and cube : "))
# val = list(map(lambda x:x(num) , func))
# print(val)    