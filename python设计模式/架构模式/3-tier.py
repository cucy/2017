#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/5/16 16:19
# Author: zhourudong

class Data:
    """ data store class"""

    products = {
        "milk": {'price': 1.50, 'quantity': 10},
        "eggs": {'price': 0.20, 'quantity': 100},
        "cheese": {'price': 2.50, 'quantity': 10},
    }

    def __get__(self, obj, klas):
        print("(从存储获取数据)")
        return {'products': self.products}


class BusinessLogic:
    """ Business logic holding data store instances """
    '''持有数据存储实例的业务逻辑'''
    data = Data()

    def product_list(self):
        return self.data['products'].keys()

    def product_information(self, product):
        return self.data['products'].get(product, None)


class Ui:
    '''UI interaction class'''
    ''' ui 接口信息类 '''

    def __init__(self):
        self.business_logic = BusinessLogic()

    def get_product_list(self):
        print('产品列表:')
        for product in self.business_logic.product_list():
            print(product)
        print('')

    def get_product_information(self, product):
        product_info = self.business_logic.product_information(product)
        if product_info:
            print('产品信息:')
            print('名字: {0}, 价格: {1:.2f}, 数量: {2:}'.format(
                product.title(), product_info.get('price', 0),
                product_info.get('quantity', 0)))
        else:
            print('"{0}" 产品不存在'.format(
                product))


def main():
    ui = Ui()
    ui.get_product_list()
    ui.get_product_information('cheese')
    ui.get_product_information('eggs')
    ui.get_product_information('milk')
    ui.get_product_information('arepas')


if __name__ == '__main__':
    main()


'''
产品列表:
(从存储获取数据)
eggs
milk
cheese

(从存储获取数据)
产品信息:
名字: Cheese, 价格: 2.50, 数量: 10
(从存储获取数据)
产品信息:
名字: Eggs, 价格: 0.20, 数量: 100
(从存储获取数据)
产品信息:
名字: Milk, 价格: 1.50, 数量: 10
(从存储获取数据)
"arepas" 产品不存在
'''