from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name = 'openhospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    _order = 'date desc'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'openhospital.appointment') or _('New')

        result = super(HospitalAppointment, self).create(vals)
        return result

    name = fields.Char(
        string='Appointment ID', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New')
    )
    patient_id = fields.Many2one(
        'openhospital.patient', string='Patient', required=True
    )
    patient_age = fields.Integer(string='Age', related='patient_id.age')
    date = fields.Date(string='Date', required=True)
    notes = fields.Text(string='Registration Notes')