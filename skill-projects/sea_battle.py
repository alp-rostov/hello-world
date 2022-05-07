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
    def __init__(self, S:list):
        self.S=S #спискок координат

    @property
    def side_(self):
        return self.S

    @side_.setter
    def side_(self,value):
        self.S =value






d1=Ship([[1,1],[1,2]])
d2=Ship([[6,6]])



print(d1.S[1][1])


D=[['0' for i in range(6)] for i in range(6)]

for i in d1.S:
    D[i[0]-1][i[1]-1]='x'
for j in d2.S:
    D[j[0]-1][j[1]-1]='x'


D_Field=PlayingField(D)

D_Field.ShowField()