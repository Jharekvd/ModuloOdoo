from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'  # Esto extiende el modelo 'sale.order'

    return_date = fields.Date(string='Return Date')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('sale', 'Sale'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft')
    sale_order_line = fields.One2many(
         'sale.order.line', 
         'order_id', 
         string='Líneas de Pedido'
    )

    aplicar_descuento_devolucion = fields.Boolean('Aplicar descuento de devolución')
    is_returned = fields.Boolean('Is Returned', default=False)
# Extiende el modelo sale.order.line
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    order_id = fields.Many2one('sale.order', string='Orden de Venta', onupdate='cascade')
  