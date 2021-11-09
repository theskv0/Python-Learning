# def is_palindrom(word) :
#     reversed_string = word[::-1]
#     if word == reversed_string :
#         return True
#     else :
#         False

# print(is_palindrom('naman'))

# # fibonacci series
# # 0, 1, 1, 2, 3, 5, 8, 13...
# def fibonacci(n) :
#     first_num, second_num = 0, 1
#     result = []
#     for i in range(1, n+1) :
#         if i == 1 :
#             result.append(first_num)
#         elif i == 2 :
#             result.append(second_num)
#         else :
#             last_num = first_num + second_num
#             result.append(last_num)
#             first_num = second_num
#             second_num = last_num
#     return result
    
# print(fibonacci(10))


# def default_params(name, age=18, hobby=None):
#     print(name)
#     print(age)
#     print(hobby)

# default_params('sumit')
# default_params('sumit', 25, 'cricket')

# # function returning two value
# def func (a, b) :       # funciton returing a tuple
#     sum = a + b
#     multi = a * b
#     return sum, multi
# print(func(2, 3))