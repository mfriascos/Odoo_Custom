# -*- coding: utf-8 -*-

{
    'name': 'Pet Store',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage products for a pet store',
    'description': """
        This module allows you to manage products for a pet store, including pets, food, toys, etc.
    """,
    'author': 'Mario Riascos',
    'website': 'http://mfriascos.github.io',
    'depends': ['base'],
    'data': [
        'views/product_view.xml',
        'views/pet_menu.xml',
        'securtiy/ir.model.access.csv',
    ],  
    # 'installable': True,
    # 'application': False,
    # 'auto_install': False,
}