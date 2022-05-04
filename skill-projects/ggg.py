# ВЫЧИСЛЕНИЕ СИНУСА по Тейлору
#
# import math
# grad=60
# b=math.radians(grad)
#
# print(grad,' градусов переведем в радианы ->',b)
# print('Синус по встроенной функции из библиотеки math -->> sin',grad,'=',math.sin(b))
#
# def rec_fibb(i):
#   B = math.radians(grad)
#   if i<6:
#       return B
#   else:
#       return rec_fibb(i-4)+B**(i-4)/math.factorial(i-4)-B**(i-6)/math.factorial(i-6)
#
# print('Синус считается с по формуле тейлора с помощью рекурсии: sin',grad,'=', rec_fibb(29))
#
#

# import math
# def sinus(x):
#
#     for i in range(3,25,4):
#         x+=-x**i/math.factorial(i)+x**(i+2)/math.factorial(i+2)
#
#     return x
# c=math.sin(b)
#
# print('Синус считается в цикле по формуле тэйлора sin=:',grad,'=',sinus(b))


# ___________________________________________________________________________________
import time


# def decorator_time(fn):
#     def wrap(arg):
#         return round(fn(arg),2)
#     return wrap
#
# @decorator_time
# def s(x):
#     return x**3
#
# print(s(2.3333))


#
# def sin_rec(x=60):
#     import math
#     x = math.radians(x)
#     for i in range(3, 25, 4):
#         x+=-x**i/math.factorial(i)+x**(i+2)/math.factorial(i+2)
#     return x

# in_build_pow = decorator_time(sin_rec)
#
#
# print(in_build_pow)
# # Запустилась функция <function in_build_pow at 0x7f938401b620>
# # Функция выполнилась. Время: 0.0000021458

# i=0
# while True:
#     a=[]
#     if  id(i) not in a and i<100:
#         a.append(id(i))
#         print(id(i))
#         i+=1
#     else:
#           break

# a = 0
# b = 0
#
# while id(a) == id(b):
#     a -= 1
#     b -= 1
#
# print(a)
#
# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print(True if list_id_after==list_id_before else False)
# print(list_id_before)
# print(list_id_after)

#
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#
# a_and_b = a_set.intersection(b_set)
#
# print(a_set)

def D(a, b, c):
    return b ** 2 - 4 * a * c

def quadratic_solve(a, b, c):
    if D(a, b, c) < 0:
        return "Нет вещественных корней"
    elif D(a, b, c) == 0:
        return -b / (2 * a)
    else:
        return (-b - D(a,b,c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)
#
# L = list(map(float, input().split()))
M = {'a': 2,
     'b': 4,
     'c': 1}

print(quadratic_solve(M[*a]))
print(M)