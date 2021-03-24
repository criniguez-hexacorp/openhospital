from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = 'openhospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    _rec_name = 'name'

    @api.depends('age')
    def _set_age_group(self):
        for rec in self:
            if rec.age:
                if rec.age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'
            else:
                rec.age_group = ''

    name = fields.Char(string='Name', required=True)
    name_seq = fields.Char(
        string='Patient ID', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New')
    )
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female')],
        default='male'
    )
    age = fields.Integer(string='Age')
    age_group = fields.Selection(
        string='Age Group',
        selection=[('major', 'Major'), ('minor', 'Minor')],
        compute='_set_age_group'
    )
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'openhospital.patient') or _('New')

        result = super(HospitalPatient, self).create(vals)
        return result
