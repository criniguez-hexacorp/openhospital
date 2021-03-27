from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = 'openhospital.doctor'
    _description = 'Openhospital Doctor'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female')],
        default='male'
    )
    user_id = fields.Many2one('res.users', string='Related User')
