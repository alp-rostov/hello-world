
class PlayingField(): # класс иговых полей
    def __init__(self, A):
        self.A=A

    def ShowField(self):
        print ( '   1   2   3   4   5   6')
        count=1
        for i in self.A:
            print(str(count)+'  '+" | ".join(i))
            count+=1


B=[['0' for i in range(6)] for i in range(6)]

Field=PlayingField(B)

Field.ShowField()