from odoo import models, fields

class Mahasiswa(models.Model):
    _name = 'student.detail'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    address = fields.Char(string="Address")
    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female')
        ],
        string="Gender", default='male'
    )