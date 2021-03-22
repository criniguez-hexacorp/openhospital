from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'openhospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')
