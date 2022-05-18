import random
from application.exceptions import *
class Dot:  #объект точки
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def __repr__(self):
        return f"({self.x},{self.y})"

#_________Проверка класса Dot:___________________
if __name__ == '__main__':
    a=Dot(1,2)
    print(f'Dot {a}')
#________________________________________________

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

#_________Проверка класса Ship:___________________
if __name__ == '__main__':
    b=Ship(Dot(1,2),3,1)
    c=b.dots
    print(f'Ship.dots {c}')
    print(f'Ship.shooten {b.shooten(Dot(1,2))==True}')
#________________________________________________

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

#_________Проверка класса Board:___________________
if __name__ == '__main__':
    v=Board()
    print ( f'Board.out {v.out(Dot(0,5))==False}' )
    v.add_ship (b)
    print (f'Board.add_ship \n{v}')
    print(f'Board.contur {v.busy }')
    v.begin()
    print ( f'Board.shot:')
    print (v.shot(Dot(1,3)))
#________________________________________________

class Player:                              # объект игрок, параметры две доски своя и компа
    def __init__(self, board:Board, enemy:Board):
        self.board = board
        self.enemy = enemy
    def ask(self):
        raise NotImplementedError()  #?Исключение, возникающее в случаях, когда наследник класса не переопределил метод, который должен был.
    def move(self):                  # метод
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
        co = self.random_board()
        co.hid=True
        self.ai=AI(co,pl)             #Объект AI(Player)
        self.us = User ( pl, co )
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
                print('Выйграл пользоватедль')
                break
            if self.us.board.count==7:
                print('Выйграл компьютер')
                break
    def start(self):
        self.greet()
        self.loop()