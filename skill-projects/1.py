import time
import math

N = 100000

def decorator_time(fn):
   def wrapp(*arg, **kwargs):
       t0 = time.time()
       result = fn(*arg, **kwargs)
       dt = time.time() - t0
       # print(f'Результат функции:{result}. Фуyкция выполняналст {dt} секунд')
       return dt
   return wrapp

def round_(fn):
    def wrap(x):
        return  round(fn(x),6)
    return wrap

import math

@decorator_time
def sin_math(x):
    x = math.radians(x)
    return math.sin(x)

grad=30
B = math.radians(grad)

@decorator_time
def sin_rec(i=15):
    if i<6:
        return B
    else:
        return sin_rec(i-4)+B**(i-4)/math.factorial(i-4)-B**(i-6)/math.factorial(i-6)

@decorator_time
def sinus(x=30):
    import math
    x = math.radians(x)
    for i in range(3, 25, 4):
        x+=-x**i/math.factorial(i)+x**(i+2)/math.factorial(i+2)
    return x


mean_pow_2 = 0
mean_in_build_pow = 0
cik=0
for i in range(N):
    mean_pow_2 += sin_rec(21)
    mean_in_build_pow += sin_math(30)
    cik += sinus(30)

print(f"Функция {sinus} выполнялась {N} раз. Среднее время: {cik / N:.20f}")
print(f"Функция {sin_rec} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.20f}")
print(f"Функция {sin_math} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.20f}")