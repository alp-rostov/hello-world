#game "15"
import random

class game_field():
    def __init__(self):
        self.sqr_={} #dictionary of cells coordinates | key - tuples of coordinates, value - index of cell

    def __str__(self):
        self.sqr_str={}
        for i, k in self.sqr_.items():
            if 0<k<10:
                k_=' '+str(k)
            elif k==0:
                k_ = ' ■'
            else:
                k_ = str ( k )

            self.sqr_str[i] = k_


        res =  f' {self.sqr_str[(0, 0)]} | {self.sqr_str[(0, 1)]} | {self.sqr_str[(0, 2)]} | {self.sqr_str[(0, 3)]}\n' \
               f' {self.sqr_str[(1, 0)]} | {self.sqr_str[(1, 1)]} | {self.sqr_str[(1, 2)]} | {self.sqr_str[(1, 3)]}\n' \
               f' {self.sqr_str[(2, 0)]} | {self.sqr_str[(2, 1)]} | {self.sqr_str[(2, 2)]} | {self.sqr_str[(2, 3)]}\n' \
               f' {self.sqr_str[(3, 0)]} | {self.sqr_str[(3, 1)]} | {self.sqr_str[(3, 2)]} | {self.sqr_str[(3, 3)]}\n'
        return res

    def random_sqr(self): #random generation of cells on the field
        l = list ( range ( 0, 16 ) )
        random.shuffle ( l )
        _=0
        for i in range(0,4):
            for j in range(0,4):
                self.sqr_[(i,j)]=l[_]
                _+=1

    def get_key(self, d:dict, value): #key definition by value in dictionary
        for k, v in d.items ( ):
            if v == value:
                return k

    def move(self): #move of cells on the field
        k=self.get_key(self.sqr_, 0)
        a=[]

        if k[1]<3:
            a.append(self.sqr_[(k[0],k[1]+1)])
        if k[1] > 0:
            a.append(self.sqr_[(k[0], k[1] - 1)])

        if k[0]<3:
            a.append(self.sqr_[(k[0]+1,k[1])])
        if k[0] > 0:
            a.append(self.sqr_[(k[0]-1, k[1])])

        b=int(input(f'Введите число ячейки для смены позиции:\n' 
                    f'Доступные числа:{a}'))
        if b not in a:
            print('Неправильный ввод данных')
            return self.move ( )

        k_=self.get_key(self.sqr_, b)

        self.sqr_[k],self.sqr_[k_]=self.sqr_[k_],self.sqr_[k]
        print(self.__str__())
        return self.move()

d=game_field()
d.random_sqr()
print(d)

d.move()
print(d)



