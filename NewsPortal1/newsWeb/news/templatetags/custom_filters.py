from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def currency(value): #filter 'Гоцин Сергей Александрович' ->> 'Гоцин С.А.'
   if isinstance(value, str):
      str1 = value.split ( )
      value = str1[0] + ' '
      for i in range ( 1, len ( str1 ) ):
         value += str1[i][0] + '.'
   return value


@register.filter()
def censor(value):
   if isinstance(value, str):
      a=['хрен', 'редиска', 'тыква']
      for i in a:
         b=' '+i[0]+'*' * (len(i)-1)+' '
         value=value.replace(i, b)
   return value