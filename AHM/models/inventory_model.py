from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo import models, fields, api, exceptions

class Medicine(models.Model):
    _name = 'ahm.medicine'
    _decription = "AHM Medicine"

    med_id = fields.Integer(string="Medicine No.",required=True)
    med_name = fields.Char(string="Medicine Name",required=True)
    med_type = fields.Selection(string="Medicine Type",selection=[('injection', 'Injection'), ('tablet', 'Tablet'), ('capsule', 'Capsule'),('syrup','Syrup')],
        default='capsule')
    med_company = fields.Char(string="Medicine Company",required=True)
    price = fields.Integer(string="price",required=True)
    manu_date = fields.Date(string="Manufactering Date")
    exp_date = fields.Date(string="Expiry Date")

class Stock(models.Model):
    _name = 'ahm.stock'
    _decription = "AHM Stock"

    # name = fields.One2many(comodel_name="ahm.medicine",string="Stock Name")
    name = fields.Char(string="Stock Name")
    stock_id = fields.Many2one('ahm.bill', string="Stock No",ondelete="cascade")
    comp = fields.Char(string="Company")


class Bill(models.Model):
    _name='ahm.bill'
    _decription = "AHM Bill"

    # bill_id = fields.One2many(comodel_name="ahm.stock",string="Bill No.",inverse_name="stock_id")
    name = fields.Char(string="Name",required=True)
    comp = fields.Char(string="Company",required=True)
    price = fields.Float(string="Price",required=True)
    quantity = fields.Integer(string="Quantity",required=True)

    @api.model
    def create(self,vals):
        print("---------Successfully Create----------")
        return super(Bill, self).create(vals)

    def write(self,vals):
        # print("---------Hello World!----------",self.env['ahm.bill'].search([('name','=',"First Stock")]))
        print("---------Successfully Write!----------",self.env['ahm.bill'].browse([1,2])._context)

        return super(Bill, self).write(vals)        

    def copy(self, default=None):
        print("---------Successfully Copied!----------")
        return super(Bill, self).copy()

    def unlink(self,default=None):
        print("---------Unlinked!----------")
        return super(Bill, self).unlink()        
        