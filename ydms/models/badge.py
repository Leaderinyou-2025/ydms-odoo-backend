# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSBadge(models.Model):
	_name = "liy.ydms.badge"
	_description = u'Danh mục huy hiệu'
	_inherit = ['mail.thread']
	_order = 'name desc'

	name = fields.Char(string=u'Tên huy hiệu', required=True, tracking=True)
	desciption = fields.Char(string=u'Mô tả thêm')
	area_of_expertise = fields.Selection([
		('emotional', 'Điều tiết cảm xúc'),
		('conflict', 'Giảm mâu thuẫn gia đình'),
		('communication', 'Cải thiện giao tiếp gia đình'),
		('discovery', 'Khám phá và phát triển bản thân'),
	], default='emotional', string="Khía cạnh", required=True)

	active_image = fields.Image(string=u'Hình ảnh')
	review_image = fields.Image(string=u'Hình ảnh khi chưa đạt')
	condition = fields.Selection([
		('consecutive_attempts', 'Số lần thực hiện liên tiếp'),
		('consecutive_days', 'Số ngày thực hiện liên tiếp'),
		('points_in_week', 'Số điểm đạt được trong tuần'),
		('points_in_month', 'Số điểm đạt được trong tháng'),
		('total_points', 'Tổng điểm'),
	], default='points_in_month', string="Điều kiện đạt được", required=True)
	condition_value = fields.Float(string = u'Giá trị', digits=(10, 0))

	order_weight = fields.Integer(string=u'Thứ tự hiển thị')