# Set - An unordered collection of unique items
# Datatype - int, float, char, string

# set1 = {1, 2, 3, 2}
# print(set1)
# list1 = [1, 2, 3, 1, 3, 3, 2, 1]
# set2 = set(list1)
# print(set2)
# set1.add(4)
# # set2.remove(13)   # error
# print(set2.discard(13))    # None
# set3 = set2.copy()
# set2.clear()

# set4 = {1, 1.0, 'hello'}
# if 1 in set4 :
#     print('Yes')

# for i in set4 :
#     print(i)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# union_set = set1 | set2
# print(union_set)
# intersection_set = set1 & set2
# print(intersection_set)



################# Set Comprehension #################

# print({i**2 for i in range(1, 4)})
name = ["sumit", "verma"]
print({i[0] for i in name})
# print({i: 'even' if (i%2 == 0) else 'odd' for i in range(1, 11)})