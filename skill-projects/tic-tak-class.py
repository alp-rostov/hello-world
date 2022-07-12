A=[['-' for i in range(3)] for i in range(3)]

class sim:  #матрица А
    def __init__(self, x, y, s):
        self.x=x
        self.y=y
        self.s=s
    def __repr__(self):
        return f"({self.x},{self.y},{self.s})"


class pole ():
    def __init__(self, A_:list):
        self.A=A_

    def print_(A): # функция отображения поля...
        print ( '  0 1 2')
        print ( f'0 {A[0][0]} {A[0][1]} {A[0][2]}' )
        print ( f'1 {A[1][0]} {A[1][1]} {A[1][2]}' )
        print ( f'2 {A[2][0]} {A[2][1]} {A[2][2]}' )
















def input_poz(n, A): #функция ввода и проверки данных n - номер игрока
    while True:
        koord=input(f'Ход игрока №{n}: введите координаты через пробел: первое число строка, воторое - столбец: ')
        b=list(koord.split ( ))
        if len(b)==2 and b[0] in ['0','1','2'] and b[1] in ['0','1','2']:
            b=list(map(int,koord.split()))
            if A[b[0]][b[1]]!='-':
                print('Ошибка! Данная ячейка занята, введите другие координаты')
                return input_poz(n, A)
            return b
        else:
            print('Ошибка! Некорректные данные')

def transpouse(mat): #трансопорирование матрицы для проверки столбцов
    matrix = []
    for i in range(len(mat[0])):
        matrix.append(list())
        for j in range(len(mat)):
            matrix[i].append(mat[j][i])
    return matrix

print('ИГРА КРЕСТИКИ-НОЛИКИ')
print('Игрок №1 - ставит "X"')
print('Игрок №2 - ставит "0"')

i=True
counter=1
while True:
    if i:
        n=1
        sim='X'
    else:
        n=2
        sim='0'
    pole (A)
    b=input_poz(n,A)

    A[b[0]][b[1]]=sim
    B = transpouse ( A )
    C = [A[0][0], A[1][1], A[2][2]]
    D = [A[2][0], A[1][1], A[0][2]]
    stroka=A[b[0]].count(sim)
    stolb=B[b[1]].count(sim)
    diagon= C.count(sim)
    diagon_ = D.count ( sim )

    if 3 in [stroka, stolb, diagon, diagon_]:
        print(f'Победа игрока №{n}. Игра окончена.')
        pole(A)
        break
    i=not i
    counter+=1
    if counter==10:
        print('Ничья. Игра окончена.')
        pole(A)
        break