value='sd редиска gewsa хрен sadv'
a=['редиска', 'хрен', 'петруша']

for i in a:
   b=' '+i[0]+'*' * (len(i)-1)+' '
   c=' '+i+' '
   value=value.replace(c, b)

print(value)