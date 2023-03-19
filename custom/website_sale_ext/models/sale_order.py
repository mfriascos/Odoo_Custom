# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:55:00 2018

@author: jose
"""

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit ='sale.order'

    to_check = fields.Boolean(string="To Check",copy=False)