# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EjPet(models.Model):
    _inherit = 'ej.pet'
    piel = fields.Char(string="Piel", size=20, default='Blue')
    paseo = fields.Boolean(string='Paseo')

    is_pretty_name = fields.Boolean(string='Is pretty name', compute="_compute_pretty_name")

    date_b = fields.Date('Fecha', default=fields.Date.today)

    @api.depends('piel', 'name')
    def _compute_pretty_name(self):
        for record in self:
            record.is_pretty_name = record.piel == 'Blue'