# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class UserRegister(http.Controller):
    @http.route('/userregister/', auth="public", type="http", csrf=False)
    def customer_index1(self, **kw):
        currency = http.request.env['res.currency'].sudo().search([]) 
        return http.request.render('AHM.customer_index1', {'currency': currency}) 

    @http.route('/registration/<string:user>',method="post" ,auth="public", type="http", csrf=False) 
    def service_provider_index1(self,user=None, **post):
        if user == 'doctor': 
            groups_id_name = [(6, 0, [request.env.ref('AHM.group_manager').id])] 
            currency_name = post.get('currency') 
            currency = request.env['res.currency'].sudo().search([('name', '=', currency_name)], limit=1) 
            partner = request.env['res.partner'].sudo().create({ 
            'name': post.get('username'), 
            'email': post.get('email') }) 
        
            company = request.env['res.company'].sudo().create({ 
            'name': post.get('username'), 
            'partner_id': partner.id, 
            'currency_id': currency.id })

            request.env['res.users'].sudo().create({ 
            'partner_id': partner.id, 
            'login': post.get('username'), 
            'password': post.get('password'),
            'company_id': company.id, 
            'company_ids': [(4, company.id)], 
            'groups_id': groups_id_name }) 
 
        else:
            groups_id_name = [(6, 0, [request.env.ref('base.group_portal').id])]
            partner = request.env['res.partner'].sudo().create({ 
                'name': post.get('username'), 
                'email': post.get('email')})
            request.env['res.users'].sudo().create({ 
                'partner_id': partner.id, 
                'login': post.get('username'), 
                'password': post.get('password'),
                'groups_id': groups_id_name }) 
        return http.local_redirect('/web/login') 