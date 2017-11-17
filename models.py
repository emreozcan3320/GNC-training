# -*- coding: utf-8 -*-
from openerp import models,fields,api

#class ismi tabloya tekabül ediyor aşağıda tanımladığımız
#field'lar ise tablo daki sutunlara denk geliyor
class employee(models.Model):

    _name = 'employee'
    _description = 'A employee register addon'

    #static fields
    name = fields.Char(string = 'Name', required = True)
    age = fields.Integer(string = 'Age')
    #asla bir record'u silme sade deacrivate et
    active = fields.Boolean(string = 'Active',default = 1)
    basic = fields.Float(string = 'Basic')
    bdate = fields.Date(string = 'BirthDate')
    jdate = fields.Date(string = 'Join Date')
    notes = fields.Text(string = 'Notes')
    template = fields.Html(string = 'Template')
    gender = fields.Sellection([('male','Male'),('female','Female')],'Gender',default='male')

    #Relation fields
    department_id = fields.Many2one("department.department_emp", "Department", domain="[('code','!=','IT')]")

    # referance_detail'daki employee_id'ye baktığımızda alt daki ref_id ile bir birlerini tamamladıklarını görürüz
    ref_ids =  fields.One2many("reference.detail", "employee_id", "References")
    # Eğer hobbies_ids deki bağlantıyı 8.0 versiyonundan daha yukarı bir versiyonda  kuruyor olsaydık ilk ve son değerler yeterli olucaktı
    hobbies_ids = fields.Many2many("hobbies.detail", "employee_hobbies_rel", "emp_id","hobbie_id", "Hobbies Info")
    responsible_id = fields.Many2one('res.partner', "Responsible Person")
    email = fields.Char(related='responsible_id.email', string="Resp Email",)
    phone = fields.Char(related='responsible_id.phone', string="RespContact")
    ref = fields.Reference(selection=[('res.partner','Partner'),('res.users','User'),('employee.employee.8','Employee')],string='Reference')

    ref_link = fields.Char("External Link")
    type = fields.Selection([('trainee','Trainee'),('probation','Probation'),('employee','Employee')], "Employee Type", default="probation")


class my_dearptment(models.Model):

    _name = 'department.department_emp'

    _rec_name = 'code'

    code = fields.Char("Code")
    name = fields.Char("Name")


class reference_detail(models.Model):

    _name = 'reference.detail'

    employee_id = fields.Many2one("employee.employee.8", "Employee", ondelete="cascade")

    name = fields.Char("Name")
    contact = fields.Char("Contact Number")
    email = fields.Char("Email")
