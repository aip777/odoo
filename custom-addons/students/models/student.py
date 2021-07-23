from odoo import api, fields, models
# ID, Name, Age, Sex, Father Name, Mother Name, Last Education
class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Student"

    id = fields.Char(string='ID', required=True)
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    father_name = fields.Char(string='Father Name', required=True)
    mother_name = fields.Char(string='Mother Name', required=True)
    last_education = fields.Char(string='Last Education', required=True)

