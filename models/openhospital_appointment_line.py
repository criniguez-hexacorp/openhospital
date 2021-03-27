from odoo import api, fields, models


class HospitalAppointmentLine(models.Model):
    _name = 'openhospital.appointment.line'
    _description = 'Openhospital Appointment Line'

    product_id = fields.Many2one('product.product', string='Medicine')
    quantity = fields.Integer(string='Quantity')
    appointment_id = fields.Many2one(
        'openhospital.appointment', string='Appointment'
    )
