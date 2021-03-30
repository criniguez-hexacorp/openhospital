from odoo import api, fields, models, exceptions, _


class HospitalPatient(models.Model):
    _name = 'openhospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    _rec_name = 'name'

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.name_seq, rec.name)))
        return res

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if rec.age <= 5:
                raise exceptions.ValidationError(
                    _('Patient age must be greater than 5')
                )

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

    @api.depends('name')
    def _compute_name_upper(self):
        for rec in self:
            rec.name_upper = rec.name.upper() if rec.name else False

    def _inverse_name_upper(self):
        for rec in self:
            rec.name = rec.name_upper.lower() if rec.name_upper else False

    def open_appointments(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'openhospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def _get_appointment_count(self):
        count = self.env['openhospital.appointment'].search_count(
            [('patient_id', '=', self.id)]
        )
        self.appointments_count = count

    @api.onchange('doctor_id')
    def _set_doctor_gender(self):
        for rec in self:
            if rec.doctor_id:
                rec.doctor_gender = rec.doctor_id.gender

    def action_patient_card_send(self):
        template_id = self.env.ref(
            'openhospital.email_template_patient_card').id
        template = self.env['mail.template'].browse(
            template_id)
        template.send_mail(self.id, force_send=True)

    name = fields.Char(
        string='Name', required=True, track_visibility='always'
    )
    name_seq = fields.Char(
        string='Patient ID', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New')
    )
    name_upper = fields.Char(
        string='Name Upper', compute='_compute_name_upper', inverse='_inverse_name_upper'
    )
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female')],
        default='male'
    )
    age = fields.Integer(string='Age', track_visibility='always')
    age_group = fields.Selection(
        string='Age Group',
        selection=[('major', 'Major'), ('minor', 'Minor')],
        compute='_set_age_group'
    )
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')
    appointments_count = fields.Integer(
        string='Appointments Count', compute='_get_appointment_count'
    )
    active = fields.Boolean(string='Active', default=True)
    doctor_id = fields.Many2one('openhospital.doctor', string='Doctor')
    doctor_gender = fields.Selection(
        string='Doctor Gender',
        selection=[('male', 'Male'), ('female', 'Female')],
    )
    email = fields.Char(string='Email')
    user_id = fields.Many2one('res.users', string='PRO')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'openhospital.patient') or _('New')

        result = super(HospitalPatient, self).create(vals)
        return result
