# strings are immutable

# print("hello " + 1)     # type error
# print("hello " + str(1))
# print("hello " * 3)     # repetition

# age  =  input("your age ")
# print("your age " + age)
# print("your age " + int(age))     # error

# name, age = "sk", 25
# x = y = z = 1

# name, age = input("name and age ").split()   # saperate value by space
# name, age = input("name and age ").split(",")   # saperate value by comma

# name = "sk"
# print("hello {}".format(name))  # python 3
# print(f"hello {name} {2+2}")  # python 3.6

# lang = "python"
# print(lang[0])
# print(lang[6])  # Index Error
# print(lang[-1]) # last value
# print(lang[-7]) # Index error
# print(lang[0:2])  # py   [start arg : stop arg-1]
# print(lang[-3:6])  # hon
# print(lang[:])  # python
# print(lang[1:])  # ython
# print(lang[:3])  # pyt
# print(lang[1:5:2])  # yh  [start arg : stop arg-1 : step arg]
# print(lang[1::2])  # yhn
# print(lang[::2])  # pto
# print(lang[::-1])  # nohtyp   [::-1] == [-1::-1]

# name = "SuMit vErmA"
# print(len(name))
# print(name.count('m'))      # 1 Case sensitive
# print(name.lower())
# print(name.title())

# name = "  sumi  t "
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())
# print(name.replace(' ', ''))

# str = "he is a programmer and he is also dancer"
# print(str.replace('is', 'was'))
# print(str.replace('is', 'was', 1))
# print(str.find('is', 10))   # 3
# print(str.find('is', 10))   # 26

# name = "sumit"
# print(name.center(9, '_'), '*') # __sumit__ *

# str = "name"
# str[0] = 'N'  # Error 
# str = 'tt'
# print(str)