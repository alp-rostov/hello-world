import random

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

class Dot:  #объект точки
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def __repr__(self):
        return f"({self.x},{self.y})"

class Ship:
    def __init__(self, n:Dot , l:int, o:int ): # объект корабля. Харктеристики: начальная точка, длинна, ориентация
        self.n=n
        self.l=l
        self.o=o
        self.lives=l # жизни корабля
    @property
    def dots(self): #метод-свойство определяет координаты всех точек возвращает список объектов   Dot
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

    def shooten(self, shot:dots): #метод проверяет выстрел на попадание в корабль возвращает true если есть попадание
        return shot in self.dots

class Board: #объект доска.
    def __init__(self, hid=False, size=6):
        self.field = [['0' for i in range ( 6 )] for i in range ( 6 )] #матрица 6-6 список списков
        self.busy=[]
        self.ships=[] # список объектов кораблей ( class Ship)
        self.hid=hid
        self.size=size
        self.count=0

    def out(self,d:Dot): #метод проверки координад в интервале от 0-6. False - если Dot входит в интервал
        return not(0<=d.x<6 and 0<=d.y<6)

    def contur(self, Ship:Ship , verb=False): #метод заполняет список занятых точек. возвращает список точек объектов Dot
        near=[(-1,-1),(-1,0),(-1,1),
              (0,-1),(0,0),(0,1),
              (1,-1),(1,0),(1,1)]
        for i in Ship.dots:  #заполнение матрициы занятых точек коробля и вокруг него i - это точка из списка точек корабля
            for ix, iy in near:
                cur=Dot(i.x+ix, i.y+iy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y]="."
                    self.busy.append ( cur )


    def add_ship(self,ship): #добавление кораблей на игровое поле
        for i in ship.dots: #берет точки от корабля
            if self.out(i) or i in self.busy: #проверяет на принадлежность полю и списку занятых точек
                raise BoardWrongShipException()
        for i in ship.dots:
            self.field[i.x][i.y]="■" #добавление на игровое поле
            self.busy.append(i)  #добавление в список занятых позиций
        self.ships.append(ship) #добавление в список кораблей
        self.contur(ship)  #добавлеят в список занятых точек (busy) точки вокруг добавленного корабля

    def __str__(self): # вывод поля на экран
        res=''
        res+='   1   2   3   4   5   6'
        count=1
        for i in self.field:
            res+='\n'+str(count)+'  '+" | ".join(i)
            count+=1
        if self.hid:
            res=res.replace("■","O")
        return res

    def shot(self, i:Dot):               # метод  проверки выстрела
        if self.out(i):                  # проверяет на выстрел в пределах поля
            raise BoardOutException ( )
        if i in self.busy:               #проверка выстрела в занятую клетку
            raise BoardUsedException
        self.busy.append(i)              #добавление в список занятных клеток
        for ship in self.ships:          # берем корабль с точками из спика кораблей
            if i in ship.dots:           # берем точку у корабля и проверяем ее с точкой выстрела
                ship.lives-=1            # отнимается жизнь у корабля объекта который взяли из списка
                self.field[i.x][i.y]='X' #вставляем в матрицу выстрел
                if ship.lives==0:
                    self.count+=1         #число убитых кораблей
                    self.contur(ship, True) # вокруг убитого корабля ставит точки
                    print("Корабль уничтожен")
                    return False #
                else:
                    print("Корабль ранен")
                    return True            # ход повторно при ранении корабля
        self.field[i.x][i.y]='.'
        print("Мимо")
        return False

    def begin(self):                       #метод возвращает пустую матрицу занятых клетокbusy
        self.busy=[]

class Player:                              # объект игрок, параметры две доски своя и компа
    def __init__(self, board:Board, enemy:Board):
        self.board = board
        self.enemy = enemy
    def ask(self):
        raise NotImplementedError()  #?Исключение, возникающее в случаях, когда наследник класса не переопределил метод, который должен был.
    def move(self):                  # метод ?????????????
        while True:
            try:
                target=self.ask()
                repeat=self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):  #делает ход комп. генерация случайных чисел возвращает точку
    def ask(self):
        d=Dot(random.randint(0,5), random.randint(0,5))
        print(f'Ход компьютера: {d.x+1} {d.y+1}')
        return  d
class User(Player): #ход игрока
    def ask(self): #метод возвращает объект точку Dot
        while True:
            cords=input('Ваш ход:').split( )
            if len(cords)!=2:
                print('Введите две координаты!')
                continue                            #Оператор continue начинает следующий проход цикла, минуя оставшееся тело цикла
            x,y= cords
            if not (x.isdigit()) or not (y.isdigit()):
                print('Введите числа')
                continue
            x,y= int(x),int(y)
            return Dot(x-1,y-1)
class Game:
    def __init__(self, size=6):
        self.size=size
        pl=self.random_board()
        pl.hid=False
        co = self.random_board()
        co.hid=True
        self.ai=AI(co,pl)             #Объект AI(Player)
        self.us = User (pl, co)
    def random_board(self): #  метод гет для объекта доска???
        board=None
        while board is None:
            board=self.random_place()
            return board
    def random_place(self): # метод установки кораблей на доску, возвращает доску с кораблями
        lens=[3,2,2,1,1,1,1]
        board=Board(6)
        attemts=0
        for l in lens: #берется корабль из списка lens
            while True:
                attemts+=1
                if attemts>2000:
                    return None
                ship=Ship(Dot(random.randint(0,self.size),random.randint(0,self.size)),l,random.randint(0,1)) # генерируется случайно корабль
                try:
                    board.add_ship(ship)  # попытка добавить на доску если попытка неудачная то отлавливается ошибка указанная в методе add_ship
                    break
                except BoardWrongShipException:
                    pass
        board.begin()  #обнуляется список занятых ячеек
        return board

    def greet(self):
        print('Приветствуем Вас в игре "МОРСОКОЙ БОЙ"!')
    def loop(self):
        num=0
        while True:
            print('-'*20)
            print('Доска пользователя')
            print(self.us.board)
            print ( '-' * 20 )
            print ( 'Доска компьютера' )
            print ( self.ai.board )
            if num%2==0:
                print('Ходит пользователь')
                repeat=self.us.move()
            else:
                print ( 'Ходит компьютер' )
                repeat = self.ai.move ( )
            if repeat:
                num-=1
            if self.ai.board.count==7:
                print('ВЫйград пользоватедль')
                break
            if self.us.board.count==7:
                print('ВЫйград комп')
                break
    def start(self):
        self.greet()
        self.loop()

g=Game()
g.start()

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
