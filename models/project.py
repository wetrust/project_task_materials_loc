# -*- coding: utf-8 -*-
# (c) 2016 Nueva Gestión - Jonathan Gutiérrez
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields

class ProjectTaskMaterials(models.Model):
	_inherit = "project.task.materials"
	location = fields.Many2one('stock.location', 'Location', required=True)

	def _prepare_stock_move(self):
		res = super(ProjectTaskMaterials, self)._prepare_stock_move()
		res['location_id'] = self.location.id

		return res
