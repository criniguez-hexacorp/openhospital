from odoo import models


class PatientCardXLSX(models.AbstractModel):
    _name = 'report.openhospital.report_patient_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({
            'font_size': 14, 'align': 'vcenter', 'bold': True
        })
        format2 = workbook.add_format({
            'font_size': 10, 'align': 'vcenter'
        })
        sheet = workbook.add_worksheet('Patient Card')
        sheet.set_column(2, 2, 30)
        sheet.set_column(3, 3, 50)
        sheet.write(2, 2, 'Name', format1)
        sheet.write(2, 3, lines.name, format2)
        sheet.write(3, 2, 'Age', format1)
        sheet.write(3, 3, lines.age, format2)
