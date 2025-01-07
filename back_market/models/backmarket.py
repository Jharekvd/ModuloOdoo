from odoo import models, fields, api

class Back_Market(models.Model):
    _name = 'back_market.back_market'
    _description = 'Gestión de Backmarket'

    product_id = fields.Many2one('product.product', string='Producto', required=True, onupdate='cascade')
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    sale_id = fields.Many2one('sale.order', string='Orden de Venta')
    return_date = fields.Date(related='sale_id.return_date',string='Fecha de Devolución',store=True)
    discount_applied = fields.Boolean(string='Descuento Aplicado')
    sale_order_line = fields.One2many(
         'sale.order.line', 
         'order_id', 
         string='Líneas de Pedido'
    )

    price_after_discount = fields.Float(
        string='Precio Final con Descuento', 
        compute='_compute_price_after_discount',
        store=True
    )
    status = fields.Selection([
        ('processing', 'En Proceso'),
        ('completed', 'Completado'),
        ('returned', 'Devuelto')
    ], string='Estado', default='processing')

    aplicar_descuento_devolucion = fields.Boolean(
        string="Aplicar descuento por devolución"
    )

    # El campo is_returned ahora está en el modelo back_market.back_market
    is_returned = fields.Boolean(string="Producto Devuelto")

    @api.depends('sale_order_line.price_unit', 'aplicar_descuento_devolucion')
    def _compute_price_after_discount(self):
        for record in self:
            total_price = 0
            for line in record.sale_order_line_ids:
                total_price += line.price_unit
            if record.aplicar_descuento_devolucion:
                total_price *= 0.8  # Aplica un descuento del 20%
            record.price_after_discount = total_price

    def apply_discount(self):
        for record in self:
            if record.sale_id:
                for line in record.sale_id.order_line:
                    if line.product_id.is_returned:
                        # Aplica un descuento del 20% si el producto es devuelto
                        line.price_unit *= 0.8

class ProductTemplate(models.Model):
        _inherit = 'product.product'
    
        is_returned = fields.Boolean(string="Producto Devuelto", default=False)
