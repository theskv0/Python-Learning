# Dictionary
#  An unordered collection of data in key value pair. 
#  We use dictionary because of limitations of lists, lists are not enough to represent real data.

# dict1 = {'name' : 'Sumit', 'age' : 25}
# dict2 = dict(name = 'Sumit', age = 25, interests = {'movies' : ['abcd', 'abcd2'], 'games' : ['cricket', 'bgmi']})
# print(type(dict1))
# print(dict2)
# print(dict2['name'])
# print(dict2['interests']['games'])
# dict1['name'] = 'Sumit Verma'   # add or update
# print(dict1)

# dict2 = {
#     'name' : 'Sumit', 
#     'age' : 25, 
#     'interests' : {
#         'movies' : ['abcd', 'abcd2'], 
#         'games' : ['cricket', 'bgmi']
#     }
# }

# if 'name' in dict2 :        # check for key
#     print(dict2['name'])

# if 'Sumit' in dict2.values() :        # check for value (with datatype)
#     print(type(dict2.values()))

# for i in dict2 :    # for keys, you can also use dict2.keys()
#     print(i)

# for i in dict2.values() :    # for values
#     print(i)

# for key, value in dict2.items() :
#     print(f"{key} : {value}")

# dict2['occupation'] = 'IT profetional'
# print(dict2.pop('interests'))
# print(dict2)
# # delete last/random item
# print(dict2.popitem())

# dict2 = {
#     'name' : 'Sumit', 
#     'age' : 25, 
#     'interests' : {
#         'movies' : ['abcd', 'abcd2'], 
#         'games' : ['cricket', 'bgmi']
#     }
# }
# dict3 = {'name' : 'Sumit Verma', 'occupation' : 'IT Profetional'}
# dict2.update(dict3)   # it will add occupation and update name
# print(dict2)

# # dict.fromkeys(iterable, value)
# d = dict.fromkeys(['name', 'age'], 'unknown')
# print(d)

# dict4 = {'name' : 'Sumit'}
# # print(dict4['age'])     # error
# print(dict4.get('age'))     # None    --  dict.get('key', 'Default Value')
# dict4.clear()       # clear all 
# dict5 = dict4   # pass by reference
# dict6 = dict4.copy()   # pass by value
# print(dict5 is dict4)
# print(dict6 is dict4)



################# Dictionary Comprehension #################

# print({i : i**2 for i in range(1, 4)})
# name = "sumit verma"
# print({i : name.count(i) for i in name})
# print({i: 'even' if (i%2 == 0) else 'odd' for i in range(1, 11)})