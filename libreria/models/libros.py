from odoo import models, fields

#creando un modelo a partir de una clase
class Libros(models.Model):
    _name = 'libros'

    name = fields.Char(string="Nombre del libro", required=True)
    editorial = fields.Char(string="editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    
    
    
