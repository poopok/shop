from rest_framework import serializers
from .models import Item, Category
from django.contrib.auth.models import User


class CategoryListViewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class ItemListViewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'image_url', 'description', 'category')


# class ItemDetailViewSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = Item
#         fields = ('name', 'price', 'image_url', 'description', 'category')


# class ItemAddViewSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('name', 'price', 'image_url', 'description', 'category')


class CategoryAddViewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'parent')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
