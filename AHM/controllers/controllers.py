# -*- coding: utf-8 -*-
from odoo import http

class Medicine(http.Controller):
    @http.route('/Medicine/Medicine', auth="public", website=True)
    def index(self, **kw):
        stock = http.request.env['ahm.stock']
        return http.request.render('AHM.index',{'stock': stock.sudo().search([])})
    

    @http.route(['/delete/<model("ahm.stock"):doc>',], auth='public', website=True)
    def delete(self,doc):
        doc.unlink()
        return http.request.redirect('/Medicine/Medicine')


    @http.route(['/update/<model("ahm.stock"):d>','/create/'], auth='public', website=True)
    def update(self,d=None):
        return http.request.render('AHM.index1',{"d" : d})

     
    @http.route(['/save/',], auth='public', website=True)
    def save(self,**kw):
        stock = http.request.env['ahm.stock']
        if kw['id']:
            stock.search([]).browse([kw['id']]).write(kw)
        else:
            stock.create(kw)
        return http.request.redirect('/Medicine/Medicine')

class Bill(http.Controller):
    @http.route('/Bill/', auth="public", website=True)
    def index(self, **kw):
        bill = http.request.env['ahm.bill']
        return http.request.render('AHM.indexbill',{'bill' : bill.sudo().search([])})

    @http.route(['/delete/<model("ahm.bill"):doc>',], auth='public',website=True)
    def delete(self,doc):
        doc.unlink()
        return http.request.redirect('/Bill/')

    @http.route(['/update/<model("ahm.bill"):d>','/create/'], auth='public', website=True)
    def update(self,d=None):
        return http.request.render('AHM.index2',{"d" : d})

    @http.route(['/save/',],auth='public', website=True)
    def save(self,**kw):
        bill = http.request.env['ahm.bill']
        if kw['id']:
            bill.search([]).browse([kw['id']]).write(kw)
        else:
            bill.create(kw)
        return http.request.redirect('/Bill/')

        