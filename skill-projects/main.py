text1='Привет рассказ ПППетя!'+' '
b=[]
j=1
str1=''
count=1
while len(text1)>1:
    if text1[0]==text1[1]:
        count+=1
    else:
        str1+=text1[0]+str(count)
        count=1
    text1 = text1[1::]
print(str1)



