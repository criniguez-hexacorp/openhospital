from odoo import api, fields, models


class HospitalAppointmentCreate(models.TransientModel):
    _name = 'openhospital.appointment.create'

    patient_id = fields.Many2one('openhospital.patient', string='Patient')
    date = fields.Date(string='Date')
