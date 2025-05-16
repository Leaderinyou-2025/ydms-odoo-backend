# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSExperienceReview(models.Model):
	_name = "liy.ydms.experience.review"
	_description = u'Đánh giá'
	_inherit = ['mail.thread']
	_order = 'experience_id desc'

	experience_id = fields.Many2one('liy.ydms.experience', string=u'Chia sẻ')
	review = fields.Selection([
		('like', 'Like'),
		('love', 'Love'),
	], default='like', string="Đánh giá", required=True)
