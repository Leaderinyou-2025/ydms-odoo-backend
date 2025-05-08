# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSPartner(models.Model):
	_description = u'YDMSPartner'
	_inherit = ['res.partner']
	_order = 'nickname asc'

	avatar = fields.Many2one('liy.ydms.avatar', string='Hình ảnh đại diện')
	nickname = fields.Char(string=u'Biệt danh', tracking=True)
	is_board_manager = fields.Boolean(u'Lãnh đạo nhà trường', default = False)
	is_teacher = fields.Boolean(u'Giáo viên', default = False)
	is_teenager = fields.Boolean(u'Học sinh', default = False)
	is_parent = fields.Boolean(u'Cha mẹ/Người bảo trợ', default = False)
	is_expert = fields.Boolean(u'Chuyên gia', default = False)

	social_id = fields.Char(string=u'Số CCCD')
	edu_id = fields.Char(string=u'Mã định danh của HS')
	teenager_code = fields.Char(string=u'Mã nội bộ HS')
