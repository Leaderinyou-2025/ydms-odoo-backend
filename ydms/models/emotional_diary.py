# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSEmotionalDiary(models.Model):
	_name = 'liy.ydms.emotional.diary'
	_description = u'Nhật ký cảm xúc'
	_inherit = ['mail.thread']
	_order = 'create_date desc'
	_rec_name = 'display_name'

	teenager_id = fields.Many2one('res.users', string=u'Học sinh', required=True)
	nickname = fields.Char(related='teenager_id.partner_id.nickname')
	question_id = fields.Many2one('liy.ydms.emotional.question', string=u'Câu hỏi', required=True)
	answer_id = fields.Many2one('liy.ydms.emotional.answer.option', string=u'Câu trả lời')

	answer_text = fields.Char(string=u'Nội dung trả lời', related='answer_id.name')
	answer_icon = fields.Image(string=u'Biểu tượng trả lời', related='answer_id.image_1920')
	rank_point = fields.Integer(related='question_id.rank_point')
	scores = fields.Integer(related='answer_id.scores')
	display_name = fields.Char(string='Tên hiển thị', compute='_compute_display_name', store=False)

	@api.depends('nickname', 'question_id.name', 'scores')
	def _compute_display_name(self):
		for rec in self:
			rec.display_name = f"{rec.teenager_id.name or 'Không rõ'} - {rec.question_id.name or ''} - {rec.scores or 0} điểm"