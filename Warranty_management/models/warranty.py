from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class Warranty(models.Model):
    _name = 'warranty.management'
    _description = 'Product Warranty Management'

    product_id = fields.Many2one('product.product', string='Producto', required=True)
    customer_id = fields.Many2one('res.partner', string='Cliente', required=True)
    sale_id = fields.Many2one('sale.order', string='Orden de Venta')
    warranty_start_date = fields.Date(string='Fecha de Inicio de Garantia', required=True)
    warranty_end_date = fields.Date(string='Fecha de Fin de Garantia', compute='_compute_warranty_end_date', store=True)
    warranty_duration = fields.Integer(string='Duracion de Garantia (meses)', default=12)
    status = fields.Selection([
        ('active', 'Activa'),
        ('expired', 'Expirada'),
        ('claimed', 'Reclamada')
    ], string='Estado', default='active')

    @api.depends('warranty_start_date', 'warranty_duration')
    def _compute_warranty_end_date(self):
        for record in self:
            if record.warranty_start_date and record.warranty_duration >0:
                start_date = fields.Date.from_string(record.warranty_start_date)
                record.warranty_end_date = start_date + relativedelta(months=record.warranty_duration)
            else:
                record.warranty_end_date = False