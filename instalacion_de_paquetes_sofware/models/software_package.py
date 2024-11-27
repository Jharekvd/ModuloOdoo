from odoo import models, fields


class instalacion_de_paquetes_sofware(models.Model):
    _name = 'instalacion_de_paquetes_sofware.instalacion_de_paquetes_sofware'
    _description = 'Gestion de paquetes'
        
    name = fields.Char(string='Programa', required=True)
    version = fields.Char(string='Version',required=True)
    product_id=fields.Many2one('product.product',string='Producto',required=True)
    software_start_date=fields.Date(string='Fecha de inicio de instalacion',required=True)
    description = fields.Text(string='Descripcion')

