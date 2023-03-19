# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Product(models.Model):
    _name = 'pet.store'
    _description = 'Pets Store'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    breed = fields.Char(string='Breed')
    price = fields.Float(string='Price')
    compute_value = fields.Float(string='Compute Value', compute='_compute_value')

    @api.depends('price')
    def _compute_value(self):
        for record in self: 
            record.compute_value = record.price * 1.10