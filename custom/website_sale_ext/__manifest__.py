# -*- coding: utf-8 -*-
{
    'name': "website_sale_ext",

    'summary':"""
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    
    'description':"""
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.mycompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/sale_order_view.xml'
        'viewa/website_sale.xml'
    ],
}