from odoo import models, fields
#importamos las carpetas models y los campos

#creamos una clase que la pasamos un modelo para crear la pagina
class instalacion_de_paquetes_sofware(models.Model):
    # nombre y descripcion de la pagina
    _name = 'instalacion_de_paquetes_sofware.instalacion_de_paquetes_sofware'
    _description = 'Gestion de paquetes software'
    # 
    name = fields.Char(string="Nombre del Software", required=True)
    version = fields.Char(string='Version',required=True)
    compatible_systems = fields.Selection(
        [('windows','Windows'),('linux','Linux'),('mac','Mac')],
        string="Sistemas Compatible",required =True
    )
    price = fields.Float(string="Precio Adicional", default=0.0)
    product_ids=fields.Many2many(
        comodel_name="product.template",
        relation="product_software_rel",
        column1="software_id",
        column2="product_id",
        string="Productos Compatibles"
    )
    software_start_date=fields.Date(string='Fecha de inicio de instalacion',required=True)
    description = fields.Text(string='Descripcion')


