from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Plantas(models.Model):
    _name = 'vivero.planta'

    name = fields.Char("Nombre de la Planta")
    price = fields.Float("Precio")
    order_ids = fields.One2many(comodel_name='vivero.pedido',inverse_name='planta_id',string='Pedidos')

class Pedidos(models.Model):
    _name = 'vivero.pedido'

    @api.constrains('qty')
    def check_qty(self):
        if self.qty < 1:
            raise ValidationError('Debe ingresar nro positivo')

    @api.onchange('qty')
    def onchange_qty(self):
        if self.qty > 0:
            self.amount_total = self.planta_id.price * self.qty

    planta_id = fields.Many2one('vivero.planta',string='Planta')
    partner_id = fields.Many2one('res.partner',string='Cliente',domain=[('customer_rank','>',0)])
    qty = fields.Integer('Cantidad')
    amount_total = fields.Float('Monto Pedido')
