# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
import math

from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSEmotionalQuestion(models.Model):
	_name = 'liy.ydms.emotional.question'
	_description = u'Câu hỏi cảm xúc'
	_order = 'name desc'

	name = fields.Char(string=u'Câu hỏi', required=True)
	encourage_interaction = fields.Char(string=u'Câu khuyến khích tương tác')
	answer_ids = fields.One2many('liy.ydms.emotional.answer.option', 'question_id', string=u'Các phương án trả lời')
	rank_point = fields.Integer(string=u'Điểm thưởng xếp hạng')
