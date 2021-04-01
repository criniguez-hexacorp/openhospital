# -*- coding: utf-8 -*-
from odoo import http


class Hospital(http.Controller):
    @http.route('/openhospital/patient/', website=True, auth='user')
    def hospital_doctor(self, **kw):
        patients = http.request.env['openhospital.patient'].sudo().search([])
        return http.request.render('openhospital.patients', {
            'patients': patients
        })
