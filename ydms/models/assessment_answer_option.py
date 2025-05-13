# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSAssessmentAnswerOption(models.Model):
	_name = 'liy.ydms.assessment.answer.option'
	_description = u'Bảng hỏi - Các phương án trả lời câu hỏi'
	_inherit = ['image.mixin']
	_order = 'name asc'

	# Master field
	question_id = fields.Many2one('liy.ydms.assessment.question', string=u'Câu hỏi', required=True)

	# Data fields
	name = fields.Char(string=u'Câu trả lời', required=True)
	scores = fields.Integer(string=u'Điểm chuyên môn', required=True)
	encourage = fields.Char(string=u'Câu động viên')
	guide_category_ids = fields.Many2many('liy.ydms.category', string=u'Hướng dẫn chuyên môn')

	order_weight = fields.Integer(string=u'Thứ tự hiển thị')