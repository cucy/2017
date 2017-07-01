#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/7/1 11:48
# Author: zhourudong


from rest_framework import serializers
from .models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'email')




