class BoardException ( Exception ):
    pass

class BoardOutException ( BoardException ):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"

class BoardUsedException ( BoardException ):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException ( BoardException ):
    pass

class Dot:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def __repr__(self):
        return f"({self.x},{self.y})"

class Ship:
    def __init__(self, n:Dot , l, o ): #начальная точка, длинна, ориентация
        self.n=n
        self.l=l
        self.o=o
        self.lives=l
    @property
    def dots(self):
        ship_dots=[]
        for i in range(self.l):
            cur_x=self.n.x
            cur_y=self.n.y
            if self.o==0:
                cur_x+=i
            elif self.o==1:
                cur_y+=i
            ship_dots.append(Dot(cur_x,cur_y))
        return ship_dots

    def shooten(self, shot:dots):
        return shot in self.dots

class Board: #
    def __init__(self):
        self.field = [['0' for i in range ( 6 )] for i in range ( 6 )]
        self.busy=[]
        self.ships=[]
    def field_show(self): #показ игровой доски
        print ( '   1   2   3   4   5   6')
        count=1
        for i in self.field:
            print(str(count)+'  '+" | ".join(i))
            count+=1

    def out(self,d:Dot):
        return not(0<=d.x<6 and 0<=d.y<6)

    def contur(self,Ship, verb=False):
        near=[(-1,-1),(-1,0),(-1,1),
              (0,-1),(0,0),(0,1),
              (1,-1),(1,0),(1,1)]
        for i in Ship.dots:  #заполнение матрициы занятых точек коробля и вокруг него
            for ix, iy in near:
                cur=Dot(i.x+ix, i.y+iy)
                if self.out(cur) and cur not in self.busy:
                if verb:
                    self.field[cur.x][cur.y]="."
                self.busy.append ( cur )
        return self.busy

    def add_ship(self,ship): #добавление кораблей на игровое поле
        for i in ship.dots: #берет точки от корабля
            if self.out(i) or i in self.busy: #проверяет на принадлежность полю и списку занятых точек
                raise BoardWrongShipException()
        for i in ship.dots:
            self.field[i.x][i.y]="■" #добавление на игровое поле
            self.busy.append(i)  #добавление в матрицу занятых позиций
        self.ships.append(ship) #добавление в список кораблей
        self.contur(ship)  #??????

    def __str__(self): # вывод поля на экран
        res=''
        res+='   1   2   3   4   5   6'
        count=1
        for i in self.field:
            res+='\n'+str(count)+'  '+" | ".join(i)
            count+=1
        return res

    def shot(self,i):
        if i in self.out ( i ):  # проверяет на выстрел в пределах поля
            raise BoardOutException ( )
        if i in self.busy:
            raise BoardUsedException #проверка выстрела в занятую клетку
        self.busy.append(i) #добавление в список занятных клеток
        for ship in self.ships: # берем корабль с точками из спика кораблей
            if i in ship.dots:  # берем точку у корабля и проверяем ее с точкой выстрела
                ship.lives-=1   # отнимается жизнь у корабля объекта который взяли из списка
                self.field[i.x][i.y]='X' #вставляем в матрицу выстрел
                if ship.lives==0:
                    self.count+=1  #число убитых кораблей
                    self.contur(ship, verb=True) # вокруг убитого корабля ставит точки
                    print("Корабль уничтожен")
                    return False #???????????????
                else:
                    print("Корабль ранен")
                    return True #??????????????????
                self.field[i.x][i.y]='.'
                print("Мимо")
                return False
    def begin(self):
        self.busy=[]

    class Player:
        def __init__(self,board, enemy):
            self.board=board
            self.enemy=enemy
        def ask(self):
            raise NotImplementedError()
        def move(self):
            while True:



s=Ship(Dot(1,2),4,1)
g=Ship(Dot(3,2),3,1)

print(s.dots)
print(g.dots)
d=Board()
d.add_ship(s)
d.add_ship(g)

print(d)

#
#
#
#
#
#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #игра морской бой
# import random
#
# class PlayingField(): # класс иговых полей
#     def __init__(self, A:list):
#         self.A=A
#     @property
#     def ShowField(self):
#         print ( '   1   2   3   4   5   6')
#         count=1
#         for i in self.A:
#             print(str(count)+'  '+" | ".join(i))
#             count+=1
#     @ShowField.setter
#     def ShowField(self,Val):
#         self.A=Val
#
#
# class Ship(): #класс кораблей
#     def __init__(self, Coordinates:list):
#         self.Coordinates=Coordinates #спискок координат
#
#     @property
#     def get_Coordinates(self):
#         return self.Coordinates
#
#     @get_Coordinates.setter
#     def set_Coordinates(self,value):
#         self.Coordinates =value
#
#
# F=[]
# ship_quantity=[[1,3],[1,2]] # количество кораблей и палуб: 1 корабль из 3-х клеток и т.д.
# for i in ship_quantity:
#     for j in range(i[0]):
#         print(f'ВВОД КООРДИНАТ КОРАБЛЯ ИЗ {i[1]} палубы')
#         Coordinates_list=[]
#         for u in range(1,i[1]+1):
#             while True:
#                 Coordinates_int = [random.randint(0,5), random.randint(0,5)]
#                 Coordinates_list.append(Coordinates_int) # заполняется список координат корабля
#                 break
#             d=Ship(Coordinates_list)
#         F.append(d)
# #
# # d1=Ship([[1,1],[1,2],[1,3]])
# # d2=Ship([[5,5],[5,6]])
# # d3=Ship([[4,1],[5,1]])
# # d4=Ship([[3,6]])
# # d5=Ship([[3,3]])
# # d6=Ship([[1,1]])
# # d7=Ship([[1,3]])
# # Fd=[d1,d2,d3,d4,d5,d6,d7]
# #
# # b1=Ship([[1,1],[1,2],[1,3]])
# # b2=Ship([[5,5],[5,6]])
# # b3=Ship([[4,1],[5,1]])
# # b4=Ship([[3,6]])
# # b5=Ship([[3,3]])
# # b6=Ship([[1,1]])
# # b7=Ship([[1,3]])
# # Fb=[b1,b2,b3,b4,b5,b6,b7]
#
#
#
# field_player=[['0' for i in range( 6 )] for i in range( 6 )] #создание поле-матрица игрока
# field_comp=[['0' for i in range( 6 )] for i in range( 6 )] #создание поле-матрица компьютера
#
#
# for j in F: #расположение кораблей игрока на игровом поле
#     for i in j.get_Coordinates:
#         field_player[i[0] - 1][i[1] - 1]= '■'
#
#
#
#
#
# print('_________________________________________________')
# print('Расположение Ваших кораблей на игровом поле')
# D_Field=PlayingField( field_player )
# D_Field.ShowField
# print('_________________________________________________')
# print('Расположение кораблей противника на игровом поле')
# D_Field1=PlayingField( field_comp )
# D_Field1.ShowField
#
# name_='Петя'
# while True:
#     print(f'{name_}, введите координаты хода')
#     while True:
#         Coordinate = input (f'введите координаты через пробел (координаты от 1 до 6)')
#         Coordinates_int = list(map(int,(Coordinate.split( ))))
#         if field_comp[Coordinates_int[0] - 1][Coordinates_int[1] - 1]== '■':
#             field_comp[Coordinates_int[0] - 1][Coordinates_int[1] - 1] = 'X'
#             D_Field1.ShowField
#             if '■' not in [*field_comp[0], *field_comp[1], *field_comp[2], *field_comp[3], *field_comp[4], *field_comp[5]]:
#                 print('Победа Игрока!')
#                 break
#         else:
#             field_comp[Coordinates_int[0] - 1][Coordinates_int[1] - 1]= 'T'
#             D_Field1.ShowField
#
#             #ход компа
#
#         while True:
#             Coordinates_int1=[random.randint(0,5),random.randint(0,5)]
#             if field_player[Coordinates_int1[0]][Coordinates_int1[1]] != '0':
#                 break
#
#         if field_player[Coordinates_int1[0]][Coordinates_int1[1]] == '■':
#             field_player[Coordinates_int1[0]][Coordinates_int1[1]] = 'X'
#             D_Field.ShowField
#             if '■' not in [*field_player[0], *field_player[1], *field_player[2], *field_player[3], *field_player[4], *field_player[5]]:
#                 print ( 'Победа Компа!' )
#                 break
#         else:
#             field_player[Coordinates_int1[0]][Coordinates_int1[1]] = 'T'
#             D_Field.ShowField
#
