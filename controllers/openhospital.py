# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Hospital(http.Controller):
    @http.route('/openhospital/patient', type='http', website=True, auth='user')
    def openhospital_patient(self, **kw):
        patients = request.env['openhospital.patient'].sudo().search([])
        return request.render('openhospital.patients', {
            'patients': patients
        })

    @http.route('/openhospital/get_patients', type='json', auth='user')
    def openhospital_get_patients(self, **kw):
        patients_rec = request.env['openhospital.patient'].search([])

        patients = []
        for rec in patients_rec:
            vals = {
                'id': rec.id,
                'name': rec.name,
                'sequence': rec.name_seq
            }
            patients.append(vals)

        data = {
            'status': 200,
            'response': patients,
            'message': 'All Patients Returned'
        }
        return data

    @http.route('/openhospital/create_patient', type='json', auth='user')
    def openhospital_create_patient(self, **rec):
        if request.jsonrequest:
            if rec['name']:
                new_patient = request.env['openhospital.patient'].sudo().create({
                    'name': rec['name'],
                    'age': rec['age'],
                    'gender': rec['gender'],
                    'email': rec['email'],
                })
                args = {
                    'success': True, 'message': 'Success', 'ID': new_patient.id
                }
            else:
                args = {
                    'success': False, 'message': 'name undefined'
                }
            return args
