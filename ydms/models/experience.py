# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSExperience(models.Model):
	_name = "liy.ydms.experience"
	_description = u'Chia sẻ kinh nghiệm'
	_inherit = ['mail.thread']
	_order = 'create_date desc'

	name = fields.Char(string=u'Tiêu đề', required=True, tracking=True)
	area_of_expertise = fields.Selection([
		('emotional', 'Điều tiết cảm xúc'),
		('conflict', 'Giảm mâu thuẫn gia đình'),
		('communication', 'Cải thiện giao tiếp gia đình'),
		('discovery', 'Khám phá và phát triển bản thân'),
	], default='emotional', string="Khía cạnh", required=True)
	parent_id = fields.Many2one('res.users', string=u'Cha mẹ')
	experience_content = fields.Html(string=u'Nội dung chia sẻ')
	attach_file = fields.Binary(u'Tài liệu đính kèm')
	review_ids = fields.One2many('liy.ydms.experience.review', 'experience_id', string='Đánh giá')
	total_like = fields.Integer(u'Số lượt Like')
	total_love = fields.Integer(u'Số lượt Love')

	status = fields.Selection([
		('wait_accept', 'Mới chia sẻ, chờ kiểm duyệt'),
		('public', 'Xuất bản'),
		('cancel', 'Nội dung không phù hợp'),
	], default='wait_accept', string="Trạng thái kiểm duyệt", required=True)

	active = fields.Boolean(u'Có hiệu lực', default=True)