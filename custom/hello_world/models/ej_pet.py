# -*- coding: utf-8 -*
from odoo import api, fields, models

class EjPet(models.Model):
    _name = 'ej.pet'
    _description = 'Pet Store Ej Pet'

    name = fields.Char(string='name', required=True)
    age = fields.Integer(string='age',required=True)
    color = fields.Char(string='color',required=True)
    is_new = fields.Boolean(string='is_new', default=True)
    type = fields.Selection([
                                ('small','Small'),
                                ('medium','Medium'),
                                ('big','Big'),
    ], string='Type', default='small', required=True)

