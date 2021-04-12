from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    company_type = fields.Selection(selection_add=[('hospital', 'Hospital')])
