# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSAssessmentResult(models.Model):
	_name = 'liy.ydms.assessment.result'
	_description = u'Dữ liệu khảo sát'
	_inherit = ['mail.thread']
	_order = 'create_date desc'

	assignee_id = fields.Many2one('res.users', string=u'Người thực hiện', required=True)
	nickname = fields.Char(related='assignee_id.nickname')
	assessment_id = fields.Many2one('liy.ydms.assessment', string=u'Bảng khảo sát')
	name = fields.Char(related='assessment_id.name', string=u'Tên bảng khảo sát')

	area_of_expertise = fields.Selection([
		('emotional', 'Điều tiết cảm xúc'),
		('conflict', 'Giảm mâu thuẫn gia đình'),
		('communication', 'Cải thiện giao tiếp gia đình'),
		('discovery', 'Khám phá và phát triển bản thân'),
	], default='emotional', string="Khía cạnh", required=True)

	answer_ids = fields.One2many('liy.ydms.assessment.answer.result', 'assessment_result_id',  string=u'Trả lời')

	rank_point = fields.Integer(related='assessment_id.rank_point')

	# Tổng điểm chuyên môn
	scores = fields.Integer(u'Điểm chuyên môn')
