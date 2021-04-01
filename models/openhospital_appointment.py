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

    def write(self, vals):
        res = super(HospitalAppointment, self).write(vals)
        return res

    def _get_default_notes(self):
        return "New Appointment"

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_delete_lines(self):
        for rec in self:
            rec.appointment_line_ids = [(5, 0, 0)]

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for rec in self:
            return {
                'domain': {
                    'order_id': [('partner_id', '=', rec.partner_id.id)]
                }
            }

    @api.model
    def default_get(self, fields):
        res = super(HospitalAppointment, self).default_get(fields)
        res['patient_id'] = self.env['openhospital.patient'].search(
            [], limit=1)[0].id
        res['notes'] = 'Default notes from default_get function'
        return res

    name = fields.Char(
        string='Appointment ID', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New')
    )
    patient_id = fields.Many2one(
        'openhospital.patient', string='Patient', required=True
    )
    patient_age = fields.Integer(string='Age', related='patient_id.age')
    date = fields.Date(
        string='Date', required=True, default=fields.Date.today
    )
    notes = fields.Text(
        string='Registration Notes', default=_get_default_notes
    )
    doctor_notes = fields.Text(string='Doctor Notes')
    pharmacy_notes = fields.Text(string='Pharmacy Notes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    appointment_line_ids = fields.One2many(
        'openhospital.appointment.line', 'appointment_id', string='Appointment Lines'
    )
    partner_id = fields.Many2one('res.partner', string='Customer')
    order_id = fields.Many2one('sale.order', string='Sale Order')
