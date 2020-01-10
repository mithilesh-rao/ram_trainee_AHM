# -*- coding: utf-8 -*-
from odoo import http

class Medicine(http.Controller):

    @http.route('/Medicine/Medicine', auth="public", type='http', website=True, csrf=False, method=['GET'])
    def index(self, **kw):
        stock = http.request.env['ahm.stock']
        return http.request.render('AHM.index',{'stock': stock.search([])})
    
    @http.route(['/delete/<model("ahm.stock"):doc>',], auth='public', website=True)
    def delete(self,doc):
        doc.unlink()
        return http.request.redirect('/Medicine/Medicine')

    @http.route(['/update/<model("ahm.stock"):doc>',], auth='public', website=True)
    def update(self,doc):
        stock.http.request.env['ahm.stock']
        return http.render.render('AHM.index.create_update_form',{"stock_id" : doc})

        # if http.request.httprequest.method == "POST":
        #   http.request.env["ahm.stock"].create({
        #       'stock_id':http.request.params.get('stock_id'),
        #       'name': http.request.params.get('txt_name'),
        #       'comp': http.request.params.get('txt_comp'),

        #   })
        # return http.request.render("AHM.index")

