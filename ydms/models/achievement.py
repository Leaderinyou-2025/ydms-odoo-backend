# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSAchievement(models.Model):
	_name = "liy.ydms.achievement"
	_description = u'Thành tích'
	_inherit = ['mail.thread']
	_order = 'create_date desc'

	area_of_expertise = fields.Selection([
		('emotional', 'Điều tiết cảm xúc'),
		('conflict', 'Giảm mâu thuẫn gia đình'),
		('communication', 'Cải thiện giao tiếp gia đình'),
		('discovery', 'Khám phá và phát triển bản thân'),
	], default='emotional', string="Khía cạnh", required=True)

	teenager_id = fields.Many2one('res.users', string=u'Học sinh', required=True)
	nickname = fields.Char(related='teenager_id.nickname', string=u'Biệt danh')
	badge_id = fields.Many2one('liy.ydms.badge', string=u'Huy hiệu đạt được')
	badge_image = fields.Image(related='badge_id.active_image', string=u'Hình ảnh huy hiệu')
	parent_id = fields.Many2one('res.users', related='teenager_id.parent_id')
