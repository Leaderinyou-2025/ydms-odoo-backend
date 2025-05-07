# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSUsers(models.Model):
	_description = u'YDMS Users'
	_inherit = ['res.users']
	_order = 'name asc'

	is_board_manager = fields.Boolean(related='partner_id.is_board_manager')
