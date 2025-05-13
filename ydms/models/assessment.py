# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSAssessment(models.Model):
	_name = 'liy.ydms.assessment'
	_description = u'Bảng hỏi'
	_order = 'name desc'

	name = fields.Char(u'Tên bảng khảo sát', required=True)
	description = fields.Char(string=u'Mô tả mục tiêu khảo sát')
	area_of_expertise = fields.Selection([
		('emotional', 'Điều tiết cảm xúc'),
		('conflict', 'Giảm mâu thuẫn gia đình'),
		('communication', 'Cải thiện giao tiếp gia đình'),
		('discovery', 'Khám phá và phát triển bản thân'),
	], default='emotional', string="Khía cạnh", required=True)

	subject = fields.Selection([
		('teenager', 'Học sinh'),
		('parent', 'Cha mẹ/Người bảo hộ'),
	], default='teenager', string=u'Đối tượng khảo sát', required=True)

	assessment_type = fields.Selection([
		('date_selector', 'Chỉ định ngày thực hiện'),
		('weekly', 'Hàng tuần'),
		('monthly', 'Hàng tháng'),
	], default='monthly', string=u'Kiểu khảo sát', required=True)

	execution_date = fields.Date(string='Ngày thực hiện khảo sát')

	question_ids = fields.One2many('liy.ydms.assessment.question', 'assessment_id', string=u'Danh sách câu hỏi')
	rank_point = fields.Integer(u'Điểm thưởng xếp hạng')

	active = fields.Boolean(u'Có hiệu lực')
