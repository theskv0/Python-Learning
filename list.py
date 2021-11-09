# ordered collection of items

# list = ['name', 12, 2.3, None]
# # append, extend, insert
# # pop, remove, del
# list.append('newitem')
# list.extend([1,2])
# list.insert(2, 'nww')
# list.pop()
# list.pop(1) # delete on index
# del list[1] # delete on index
# list.remove('anme')
# print(list)

# list = [8, 1, 3, 5, 3, 4, 22]
# if 1 in list :
#     print(True)
# print(list.count(3))  # count of 3 in list
# list.reverse()  # reverse list
# print(sorted(list)) # print in sorted order without sorting
# list.sort() # sort list
# list.clear()    # clear list
# print(list.copy())  # copy list
# print(list)

# list1 = [1, 2]
# list2 = [1, 2]
# print(list1 == list2)   # true // is values are same
# print(list1 is list2)   # false // check for same memory

# print("sumit verma".split())    # default seperater is ' ', you can use ',' 
# list = ['sumit', 'verma']
# print(','.join(list))

### List vs Array ### list module = to javascript array
# List                      Array
# Any data type             Fixed data type
# Slow                      Fast

### List vs String ### list module = to javascript String
# List                      String
# mutable                   immutable
# Any data type             Only character

# fruits = ['apple', 'banana', 'orange']
# for fruit in fruits :
#     print(fruit)
# i = 0
# while i < len(fruits) :
#     print(fruits[i])
#     i += 1

# list_inside_list = [[1, 2, 3], [4, 5, 6]]
# print(list_inside_list[1][0])

# numbers = list(range(1, 11))
# print(type(numbers))
# print(numbers.pop())    # pop last value and return
# print(numbers.index(5))     # position of value 5
# print(numbers.index(5, 2))     # (value, start, stop)
# print(min(numbers))
# print(max(numbers))
