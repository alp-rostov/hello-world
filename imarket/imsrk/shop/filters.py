from django_filters import FilterSet, CharFilter, NumberFilter
from .models import Product

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ProductFilter(FilterSet):
   field_name=CharFilter(
       field_name='name',
       label='Название продукта',
       lookup_expr='icontains'
   )
   # price=NumberFilter()
   pricelt=NumberFilter(
       field_name='price',
       lookup_expr='lt',
       label='Цена до'
   )
   pricegt = NumberFilter (
       field_name='price',
       lookup_expr='gt',
       label='Цена от'
   )
   class Meta:
       model = Product
       fields = {'name':[],
                 'price': []}
