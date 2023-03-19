# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate',
    'version': '1.0',
    'author': 'Mario Fernando Riascos',
    'maintainer': 'Mario Fernando Riascos',
    'website': 'mfriascos.github.io',
    'license': 'AGPL-3',
    'depends': ['base'], 
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'application': True,
}
