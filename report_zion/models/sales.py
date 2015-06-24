# -*- coding: utf-8 -*-
from openerp import fields, models

class sales_order_terms(models.Model):
	_inherit = 'sale.order'

	# Add a new column to the res.partner model, by default partners are not
	# instructors
	note = fields.Text(string="Terms and conditions", default="Este documento es solamente para efectos informativos y no representa una oferta o propuesta ni crea relación contractual alguna entre las partes. En caso de que los productos encontrados en esta cotización, sean requeridos por EL CLIENTE, éste se obliga a cumplir previamente con todos los requisitos de contratación, tales como: un análisis de crédito; presentación de documentación fiscal y legal; así como la suscripción del contrato que zion aplique, entre otros.")
