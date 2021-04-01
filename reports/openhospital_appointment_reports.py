from odoo import api, fields, models, _


class AppointmentReport(models.AbstractModel):
    _name = 'report.openhospital.report_appointment'
    _description = 'Appointment Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        if data['form']['patient_id']:
            appointments = self.env['openhospital.appointment'].search(
                [('patient_id', '=', data['form']['patient_id'][0])])
        else:
            appointments = self.env['openhospital.appointment'].search([])

        return {
            'doc_ids': docids,
            'doc_model': 'openhospital.patient',
            'docs': appointments,
            'data': data,
        }
