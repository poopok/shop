from rest_framework import viewsets, generics
from .serializers import *
from .models import Category, Item
from django.db.models import Q

#  Create your views here.


# Не пойму почему обычный generics.ListAPIView ругается
class CategoryListViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryListViewSerializer
    # Или так
    # filter_backends = [SearchFilter]
    # search_fields = ['name']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Category.objects.all()
        query = self.request.GET.get('q')
        # не знаю так можно заменить или нет
        # queryset_list = Category.objects.all(name=query)
        if query:
            queryset_list = queryset_list.filter(
                Q(name__incontains=query)
            ).distinct()
        return queryset_list


class ItemListViewSet(viewsets.ModelViewSet):
    serializer_class = ItemListViewSerializer
    queryset = Item.objects.all().order_by('-price')


# class ItemDetailView(generics.RetrieveAPIView):
#     serializer_class = ItemDetailViewSerializer
#     queryset = Item.objects.all()
#     lookup_field = 'name'
#     lookup_url_kwarg = 'item_name'


# class ItemAddView(generics.CreateAPIView):
#     serializer_class = ItemAddViewSerializer
#     queryset = Item.objects.all()


class CategoryAddView(generics.CreateAPIView):
    serializer_class = CategoryAddViewSerializer
    queryset = Item.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
