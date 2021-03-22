from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = 'openhospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    name_seq = fields.Char(
        string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New')
    )
    age = fields.Integer(string='Age')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'openhospital.patient') or _('New')

        result = super(HospitalPatient, self).create(vals)
        return result
