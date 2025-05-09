# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSCategory(models.Model):
	_name = "liy.ydms.category"
	_description = u'Chủ đề chuyên môn'
	_inherit = ['mail.thread', 'image.mixin']
	_order = 'name desc'

	area_of_expertise = fields.Selection([
		('emotional', 'Điều tiết cảm xúc'),
		('conflict', 'Giảm mâu thuẫn gia đình'),
		('communication', 'Cải thiện giao tiếp gia đình'),
		('discovery', 'Khám phá và phát triển bản thân'),
	], default='emotional', string="Khía cạnh", required=True)

	name = fields.Char(string=u'Tên chủ đề', required=True, tracking=True)
	desciption = fields.Char(string=u'Mô tả')
	tags = fields.Char(string=u'Từ khoá')
