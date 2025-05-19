# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSTask(models.Model):
	_name = 'liy.ydms.task'
	_description = u'Nhiệm vụ'
	_inherit = ['mail.thread']
	_order = 'create_date desc'

	area_of_expertise = fields.Selection([
		('emotional', 'Điều tiết cảm xúc'),
		('conflict', 'Giảm mâu thuẫn gia đình'),
		('communication', 'Cải thiện giao tiếp gia đình'),
		('discovery', 'Khám phá và phát triển bản thân'),
	], default='emotional', string="Khía cạnh", required=True)

	assignee_ids = fields.Many2many('res.users', string=u'Người thực hiện', required=True)
	guide_id = fields.Many2one('liy.ydms.guide', string=u'Nhiệm vụ/Hoạt động', required=True)
	name = fields.Char(u'Tên nhiệm vụ/hoạt động')
	guide_type = fields.Selection(related='guide_id.guide_type')

	task_text_result = fields.Html(u'Kết quả thực hiện (Text)')
	task_image_result = fields.Image(u'Kết quả thực hiện (Image)')
	task_percentage_result = fields.Integer(u'Kết quả thực hiện (%)')

	rank_point = fields.Integer(related='guide_id.rank_point')
	scores = fields.Integer(related='guide_id.scores')

	status = fields.Selection([
		('pending', 'Chờ thực hiện'),
		('inprogress', 'Đang thực hiện'),
		('completed', 'Hoàn thành'),
		('ignore', 'Không thực hiện'),
	], default='pending', string="Trạng thái", required=True)

