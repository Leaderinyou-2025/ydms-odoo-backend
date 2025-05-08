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

	school_id = fields.Many2one('res.partner', string='Trường học', domain="[('is_school', '=', True)]")
	classroom_id = fields.Many2one('liy.ydms.classroom', string='Trường học', domain="[('school_id', '=?', school_id)]")
	
	#Related data and store
	is_board_manager = fields.Boolean(related='partner_id.is_board_manager', stored = True)
	is_teacher = fields.Boolean(related='partner_id.is_teacher', stored = True)
	is_teenager = fields.Boolean(related='partner_id.is_teenager', stored = True)
	is_parent = fields.Boolean(related='partner_id.is_parent', stored = True)
	is_expert = fields.Boolean(related='partner_id.is_expert', stored = True)
