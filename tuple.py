# TUPLE
# any data type
# immutable - no insert, no remove
# faster
# methods - count, index, len, min, max, sum, tuple[:2]

# mixed = (1, 2, 3, 4.0)
# # Looping in tuple
# for i in mixed :
#     print(i)

# # Tuple with one element
# nums = (1)      # wrong
# nums = (1,)     # right
# print(type(nums))

# # Tuple without parenthesis
# names = 'sumit', 'kumar', 'verma'
# print(type(names))

# # Tuple unpacking
# names = 'sumit', 'kumar', 'verma'
# f_name, m_name, l_name = (names)  # variables count must be same as tuple elements count
# print(f_name)

# # List inside tuple
# favourites = ('listening', ['cricket', 'bgmi'])     # list inside tuple is also mutable
# favourites[1].append('football')
# print(favourites)

# nums = tuple(range(1, 11))
# print(nums)