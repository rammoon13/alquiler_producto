# models/alquiler_producto.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta, date

class AlquilerProducto(models.Model):
    _name = 'alquiler.producto'
    _description = 'Gestión del Servicio de Alquiler de Productos'

    name = fields.Char(string="Referencia del Préstamo", required=True)
    cliente_id = fields.Many2one('res.partner', string="Cliente", required=True)
    producto_id = fields.Many2one('product.product', string="Producto", required=True)
    fecha_inicio = fields.Date(string="Fecha de Inicio", required=True, default=fields.Date.today)
    fecha_fin = fields.Date(string="Fecha de Finalización", compute="_compute_fecha_fin", store=True)
    estado = fields.Selection([
        ('en_alquiler', 'En Alquiler'),
        ('entregado', 'Entregado'),
        ('no_entregado', 'No Entregado')
    ], string="Estado", default="en_alquiler")
    observaciones = fields.Text(string="Observaciones")

    @api.depends('fecha_inicio')
    def _compute_fecha_fin(self):
        for record in self:
            if record.fecha_inicio:
                record.fecha_fin = record.fecha_inicio + timedelta(days=30)

    @api.onchange('producto_id')
    def _onchange_producto_id(self):
        if self.producto_id and not self.producto_id.qty_available:
            raise ValidationError("Este producto no está disponible para alquiler.")

    def cron_verificar_prestamos_vencidos(self):
        prestamos = self.search([
            ('estado', '=', 'en_alquiler'),
            ('fecha_fin', '<', date.today())
        ])
        prestamos.write({'estado': 'no_entregado'})
