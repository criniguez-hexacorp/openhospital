from odoo import api, fields, models, _


class PatientReport(models.AbstractModel):
    _name = 'report.openhospital.report_patient_pdf'
    _description = 'Patient Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['openhospital.patient'].browse(docids[0])
        appointments = self.env['openhospital.appointment'].search(
            [('patient_id', '=', docids[0])])

        appointments_list = []
        for app in appointments:
            vals = {
                'name': app.name,
                'notes': app.notes,
                'date': app.date
            }
            appointments_list.append(vals)

        return {
            'doc_ids': docids,
            'doc_model': 'openhospital.patient',
            'docs': docs,
            'data': data,
            'appointments': appointments_list,
        }
