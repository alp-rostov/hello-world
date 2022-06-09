A={'a':1,'b':2,'c':3,'d':4}
B={'a':1112,'b':111,'c':13,'d':114}
min_x=min(A.keys(), key=lambda x:B[x])
print(min_x)
