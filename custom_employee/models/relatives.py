from odoo import models, fields ,api
import datetime


class Relatives(models.Model):
    _name = 'custom_employee.relatives'
    name = fields.Char(string='Name')
    dateOfBirth = fields.Date(string="Date Of Birth")
    gender = fields.Selection([('m', 'Male'),('f', 'Female')], default='m')
    age = fields.Char(compute='calc_age')
    employee_id = fields.Many2one('hr.employee')

    @api.onchange('dateOfBirth')
    def calc_age(self):
        for data in self:
            if data.dateOfBirth:
                current_year = datetime.datetime.now().year
                birth_year = datetime.datetime.strptime(data.dateOfBirth, "%Y-%m-%d").year
                age = current_year - birth_year
                data.age = age