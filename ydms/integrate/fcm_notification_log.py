# -*- coding: utf-8 -*-
###############################################################################
#
#	Công ty ALtek.
#	Development by Altek Team
#	Copyright (C) 2019 ALTEK(<http://altek.vn>).
#
###############################################################################
from odoo import fields, models, api, http, tools, _, SUPERUSER_ID
from collections import defaultdict


class YDMSFCMNotificationLog(models.Model):
	_name = "liy.ydms.notification.log"
	_description = u'Nhật kí gửi thông báo'
	_order = 'create_date desc'

	# Master field
	notification_id = fields.Many2one('liy.ydms.notification', string='Thông báo')

	# Log fields
	recipient_ids = fields.Many2one('res.partner', string=u'Người nhận')
	state = fields.Selection(selection=[('fail', 'Không thành công'), ('success', 'Thành công')],
							 string=u'Trạng thái')
	success_count = fields.Integer(string="Số lượng hoàn thành")
	fail_count = fields.Integer(string="Số lượng thất bại")
	message = fields.Text(string="Phản hồi")
	completed_on = fields.Datetime(string='Ngày hoàn thành gửi thông báo')
