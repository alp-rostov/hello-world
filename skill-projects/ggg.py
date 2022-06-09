array = [i for i in range(1000000)]

b=0
for i in range(len(array)-1):
        count = i
        cur=array[i+1]
        b+=1
        while count >=0 and cur > array[ count ]:
                array[ count+1] = array[count]
                count-= 1
                b+=1
        array[count+1]=cur


print(array)

