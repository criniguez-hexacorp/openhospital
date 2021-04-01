from odoo import api, fields, models


class HospitalAppointmentCreate(models.TransientModel):
    _name = 'openhospital.appointment.create'

    patient_id = fields.Many2one('openhospital.patient', string='Patient')
    date = fields.Date(string='Date')

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'date': self.date,
            'notes': 'Created from the wizard'
        }
        self.patient_id.message_post(
            body='Appointment Created Successfully', subject='Appointment Creation'
        )
        self.env['openhospital.appointment'].create(vals)

    def delete_patient(self):
        for rec in self:
            rec.patient_id.unlink()
