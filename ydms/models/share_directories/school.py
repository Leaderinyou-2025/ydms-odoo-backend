# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSSchool(models.Model):
	_description = u'Trường học'
	_inherit = ['res.partner']
	_order = 'name asc'

	name = fields.Char(string=u'Tên trường', required=True, tracking=True)
	code = fields.Char(string=u'Mã trường', tracking=True)
	is_school = fields.Boolean(u'Trường học', default = False, tracking=True)
	classroom_ids = fields.One2many('liy.ydms.classroom', 'school_id', string='Danh sách lớp học')
