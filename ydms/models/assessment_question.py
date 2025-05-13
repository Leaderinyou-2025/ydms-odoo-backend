# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSAssessmentQuestion(models.Model):
	_name = 'liy.ydms.assessment.question'
	_description = u'Bảng hỏi - Câu hỏi'
	_order = 'name desc'

	# Master field
	assessment_id = fields.Many2one('liy.ydms.assessment', string=u'Bảng hỏi', required=True)

	name = fields.Char(string=u'Câu hỏi', required=True)
	description = fields.Char(string=u'Hướng dẫn trả lời')

	# Kiểu câu trả lời: answer_type=input_text thì answer_ids=FALSE
	answer_type = fields.Selection([
		('option', 'Chọn phương án có sẵn'),
		('input_text', 'Nhập nội dung trả lời'),
	], default='option', string=u'Kiểu câu trả lời', required=True)

	# Chỉ áp dụng với answer_type=option
	answer_ids = fields.One2many('liy.ydms.emotional.answer.option', 'question_id', string=u'Các phương án trả lời')
	display_type = fields.Selection([
		('text_only', 'Chỉ hiển thị text'),
		('icon_only', 'Chỉ hiển thị biểu tượng'),
		('both', 'Hiển thị cả biểu tượng và text'),
	], default='text_only', string=u'Kiểu hiển thị câu trả lời', required=True)

	# Chỉ áp dụng với answer_type=input_text, nếu answer_type=option thì lấy trong phương án trả lời
	scores = fields.Integer(string=u'Điểm chuyên môn', required=True)

	order_weight = fields.Integer(string=u'Thứ tự hiển thị')

