#A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
# Sample Code

#>>> from collections import Counter
#>>> 
#>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
#>>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>> 
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>> 
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]


# Task

# Ali is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money Ali earned.
