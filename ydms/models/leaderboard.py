# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSLeaderboard(models.Model):
	_name = "liy.ydms.leaderboard"
	_description = u'Xếp hạng'
	_inherit = ['mail.thread']
	_order = 'name desc'

	name = fields.Char(string=u'Tháng', required=True, tracking=True)
	area_of_expertise = fields.Selection([
		('emotional', 'Điều tiết cảm xúc'),
		('conflict', 'Giảm mâu thuẫn gia đình'),
		('communication', 'Cải thiện giao tiếp gia đình'),
		('discovery', 'Khám phá và phát triển bản thân'),
	], default='emotional', string="Khía cạnh", required=True)
	teenager_id = fields.Many2one('res.users', string=u'Học sinh', required=True)
	nickname = fields.Char(related='teenager_id.partner_id.nickname')
	total_points = fields.Integer(u'Tổng điểm trong tháng')
	ranking = fields.Integer(u'Xếp hạng')
	rank_month = fields.Char(u'Tháng xếp hạng')
	parent_id = fields.Many2one('res.users', related='teenager_id.parent_id')

