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

    def print_report(self):
        # if self.patient_id:
        #     patient_id = self.patient_id.id
        #     appointments = self.env['openhospital.appointment'].search(
        #         [('patient_id', '=', patient_id)])
        # else:
        #     appointments = self.env['openhospital.appointment'].search([])

        # appointments_list = []
        # for app in appointments:
        #     vals = {
        #         'name': app.name,
        #         'notes': app.notes,
        #         'date': app.date
        #     }
        #     appointments_list.append(vals)

        data = {
            'model': 'openhospital.appointment.create',
            'form': self.read()[0],
            # 'appointments': appointments_list
        }
        return self.env.ref('openhospital.action_report_openhospital_appointment').report_action(self, data=data)
