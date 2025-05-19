# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSAssessmentAnswerResult(models.Model):
	_name = 'liy.ydms.assessment.answer.result'
	_description = u'Dữ liệu khảo sát - Câu trả lời'
	_inherit = ['mail.thread']
	_order = 'create_date desc'

	# Master field
	assessment_result_id = fields.Many2one('liy.ydms.assessment.result', string=u'Bảng dữ liệu khảo sát')

	question_id = fields.Many2one('liy.ydms.assessment.question', string=u'Câu hỏi', required=True)
	question_name = fields.Char(u'Tên câu hỏi')
	answer_id = fields.Many2one('liy.ydms.assessment.answer.option', string=u'Câu trả lời')
	answer_text = fields.Char(u'Nội dung trả lời (Text)')

	scores = fields.Integer(related='answer_id.scores')
