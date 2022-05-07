#игра морской бой
class PlayingField(): # класс иговых полей
    def __init__(self, A:list):
        self.A=A
    @property
    def ShowField(self):
        print ( '   1   2   3   4   5   6')
        count=1
        for i in self.A:
            print(str(count)+'  '+" | ".join(i))
            count+=1
    @ShowField.setter
    def ShowField(self,Val):
        self.A=Val


class Ship(): #класс кораблей
    def __init__(self, Coordinates:list, Сonditions: list):
        self.Coordinates=Coordinates #спискок координат
        self.Сonditions=Сonditions #состояние корабля X - палуба поражена, ■ - палуба целая

    @property
    def get_Coordinates(self):
        return self.Coordinates

    @get_Coordinates.setter
    def set_Coordinates(self,value):
        self.Coordinates =value

    @property
    def get_Сonditions(self):
        return self.Сonditions

    @get_Сonditions.setter
    def set_Сonditions(self,value):
        self.Сonditions =value


# F=[]
# ship_quantity=[[1,3],[1,2]] # количество кораблей и палуб: 1 корабль из 3-х клеток и т.д.
# for i in ship_quantity:
#     for j in range(i[0]):
#         print(f'ВВОД КООРДИНАТ КОРАБЛЯ ИЗ {i[1]} палубы')
#         Coordinates_list=[]
#         Сondition_list=[]
#         for u in range(1,i[1]+1):
#             while True:
#                 Coordinate = input (f'введите координаты палубы № {u} из {i[1]}  через пробел (координаты от 1 до 6)')
#                 Coordinates_int = list(map(int,(Coordinate.split( ))))
#                 if 1<=Coordinates_int[0]<=6 and 1<=Coordinates_int[1]<=6:
#                     Coordinates_list.append(Coordinates_int) # заполняется список координат корабля
#                     Сondition_list.append('■')                 # заполняется список состояния корабля
#                     break
#                 else:
#                     print('ВНИМАНИЕ введенные координаты выходят за пределы игрового поля! Повторите попытку.')
#         d=Ship(Coordinates_list,Сondition_list)
#         F.append(d)

d1=Ship([[1,1],[1,2],[1,3]],['■','■','■'])
d2=Ship([[5,5],[5,6]], ['■','■'])
d3=Ship([[4,1],[5,1]],['■','■'])
d4=Ship([[3,6]],['■'])
d5=Ship([[3,3]],['■'])
d6=Ship([[1,1]],['■'])
d7=Ship([[1,3]],['■'])
Fd=[d1,d2,d3,d4,d5,d6,d7]

b1=Ship([[1,1],[1,2],[1,3]],['■','■','■'])
b2=Ship([[5,5],[5,6]], ['■','■'])
b3=Ship([[4,1],[5,1]],['■','■'])
b4=Ship([[3,6]],['■'])
b5=Ship([[3,3]],['■'])
b6=Ship([[1,1]],['■'])
b7=Ship([[1,3]],['■'])
Fb=[b1,b2,b3,b4,b5,b6,b7]



D=[['0' for i in range(6)] for i in range(6)]
D1=[['0' for i in range(6)] for i in range(6)]

for j in Fd:
    count=0
    for i in j.get_Coordinates:
        D[i[0]-1][i[1]-1]=j.get_Сonditions[count]
        count= 1+count

for j in Fb:  #матрица компа
    count=0
    for i in j.get_Coordinates:
        D1[i[0]-1][i[1]-1]=j.get_Сonditions[count]
        count= 1+count


print('_________________________________________________')
print('Расположение Ваших кораблей на игровом поле')
D_Field=PlayingField(D)
D_Field.ShowField
print('_________________________________________________')
print('Расположение кораблей противника на игровом поле')
D_Field1=PlayingField(D1)
D_Field1.ShowField

name_='Петя'
while True:
    print(f'{name_}, введите координаты хода')
    while True:
        Coordinate = input (f'введите координаты через пробел (координаты от 1 до 6)')
        Coordinates_int = list(map(int,(Coordinate.split( ))))
        if D1[Coordinates_int[0]-1][Coordinates_int[1]-1]=='■':
            D1[Coordinates_int[0]-1][Coordinates_int[1]-1] = 'X'
            D_Field1.ShowField
            if '■' not in D1[0]:
                print('Победа')
        else:
            D1[Coordinates_int[0]-1][Coordinates_int[1]-1]='T'
            D_Field1.ShowField