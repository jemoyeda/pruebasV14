from odoo import models, fields

#creando un modelo a partir de una clase
class Libros(models.Model):
    _name = 'libros'

    name = fields.Char(string="Nombre del libro")
    editorial = fields.Char(string="editorial")
    
    
    
