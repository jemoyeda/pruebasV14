from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class Location(models.Model):
    _name = "hotel.location"
    _description = "Location"

    dateloc = fields.Date(string="Date debut location")
    nombre = fields.Integer(
        'Nombre de jours'
    )
    datefinloc = fields.Date(string="Date fin location", compute="_compute_datefinloc")
    prix = fields.Integer(
        'Montant location'
    )
    chambre_id = fields.Many2one(
        "hotel.chambre",
        string="Chambre",
    )
    total = fields.Integer(string="Prix total", compute="_compute_total")
    _sql_constraints = [
        ('dateloc_chambre_id_unique', 'unique (dateloc, chambre_id)', "Cette chambre est déja occuper")
    ]

    @api.depends("prix", "nombre")
    def _compute_total(self):
        for record in self:
            record.total = record.prix * record.nombre

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s-%s" % (record.dateloc, record.total)
            result.append((record.id, rec_name))
        return result

    @api.depends('dateloc', 'datefinloc', 'nombre')
    def _compute_datefinloc(self):
        for record in self:
            nb = record.nombre
            record.datefinloc = record.dateloc + relativedelta(days=nb)


