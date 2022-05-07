#игра морской бой
class PlayingField(): # класс иговых полей
    def __init__(self, A:list):
        self.A=A

    def ShowField(self):
        print ( '   1   2   3   4   5   6')
        count=1
        for i in self.A:
            print(str(count)+'  '+" | ".join(i))
            count+=1

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


F=[]
ship_quantity=[[1,3],[2,2]] # количество кораблей и палуб: 1 корабль из 3-х клеток и т.д.
for i in ship_quantity:
    for j in range(i[0]):
        print(f'ВВОД КООРДИНАТ КОРАБЛЯ ИЗ {i[1]} палубы')
        Coordinates_list=[]
        Сondition_list=[]
        for u in range(1,i[1]+1):
            Coordinate = input (f'введите координаты палубы № {u} из {i[1]}  через пробел (координаты от 1 до 6)')
            Coordinates_int = list(map(int,(Coordinate.split( ))))
            Coordinates_list.append(Coordinates_int) # заполняется список координат корабля
            Сondition_list.append('■')                 # заполняется список состояния корабля
        d=Ship(Coordinates_list,Сondition_list)
        F.append(d)
# print(F[0].side_)



D=[['0' for i in range(6)] for i in range(6)]

for j in F:
    count=0
    for i in j.get_Coordinates:
        D[i[0]-1][i[1]-1]=j.get_Сonditions[count]
        count= 1+count



D_Field=PlayingField(D)

D_Field.ShowField()