# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSGuide(models.Model):
	_name = "liy.ydms.guide"
	_description = u'Bài tập, hướng dẫn chuyên môn'
	_inherit = ['mail.thread']
	_order = 'name desc'

	name = fields.Char(string=u'Tên bài tập, hướng dẫn', required=True, tracking=True)

	guide_type = fields.Selection([
		('group_activitie', 'Hoạt động nhóm'),
		('family_activitie', 'Hoạt động gia đình'),
		('instruction', 'Hướng dẫn'),
		('exercise', 'Bài tập'),
	], default='instruction', string="Phân loại", required=True)

	area_of_expertise = fields.Selection([
		('emotional', 'Điều tiết cảm xúc'),
		('conflict', 'Giảm mâu thuẫn gia đình'),
		('communication', 'Cải thiện giao tiếp gia đình'),
		('discovery', 'Khám phá và phát triển bản thân'),
	], default='emotional', string="Khía cạnh", required=True)

	category_ids = fields.Many2many('liy.ydms.category', string=u'Chủ đề')
	desciption = fields.Char(string=u'Mô tả')
	guide_content = fields.Html(string=u'Nội dung hướng dẫn')
	guide_attachment = fields.Binary(string=u'Tài liệu đính kèm')
	rank_point = fields.Integer(string=u'Điểm thưởng xếp hạng')
	scores = fields.Integer(string=u'Điểm chuyên môn', required=True)
	age_option = fields.Selection([
		('all_age', 'Mọi lứa tuổi'),
		('within', 'Trong khoảng'),
	], default='all_age', string="Lứa tuổi", required=True)
	from_age = fields.Integer(string=u'Lứa tuổi áp dụng (Từ)')
	to_age = fields.Integer(string=u'Lứa tuổi áp dụng (Đến)')
	from_age_visible = fields.Boolean(compute="_compute_age_visibility", store=False)

	@api.depends('age_option')
	def _compute_age_visibility(self):
		for rec in self:
			rec.from_age_visible = rec.age_option == 'all_age'


