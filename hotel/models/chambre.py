from odoo import models, fields
class Chambre(models.Model):
	_name="hotel.chambre"
	_description="Chambre"

	numero = fields.Integer(
		'Numéro Chambre'
		)
	infor=fields.Char(
		string="Description Chambre"
		)

	def name_get(self):
		result = []
		for record in self:
			rec_name = "%s-%s" % (record.numero, record.infor)
			result.append((record.id, rec_name))
		return result

