#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/5/16 10:00
# Author: zhourudong

import random

''' 抽象工厂模式的实现 '''


class PetShop:
    """ 一宠物店 """

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory, we can set it at will."""
        """pet_factory是抽象工厂,我们可以随意设定"""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""
        """使用抽象工厂创建和显示宠物"""
        pet = self.pet_factory.get_pet()
        print("We have a lovely {}".format(pet))
        print("It says: {}".format(pet.speak()))
        print("We also have {}".format(self.pet_factory.get_food()))


# 我们工厂生产的东西
class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# Factory classes
class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


# Create the proper family 创造适当的家庭
def get_factory():
    return random.choice([DogFactory, CatFactory])()

# Show pets with various factories 显示宠物与各种工厂
if __name__ == '__main__':
    for i in range(2):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("=" * 20)

# 返回
'''
We have a lovely Cat
It says meow
We also have cat food
====================
We have a lovely Dog
It says woof
We also have dog food
====================
'''


# -----------------------------------
#  宠物店 订购宠物 宠物工厂生产 返回宠物 宠物特有属性
# -----------------------------------
