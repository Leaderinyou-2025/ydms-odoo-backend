# -*- coding: utf-8 -*-
from odoo import fields, models, api


class YDMSFCMNotification(models.Model):
	_name = "liy.ydms.notification"
	_description = u'Thông báo'
	_order = 'create_date desc'

	sender_id = fields.Many2one('res.users', string=u'Người gửi thông báo', required=True, default=lambda self: self.env.user)
	name = fields.Char(string='Về việc', required=True)
	description = fields.Char(string='Mô tả ngắn', required=True)
	recipient_ids = fields.Many2many('res.partner', string='Người nhận')
	body = fields.Html(string='Nội dung thông báo')
	attachment_id = fields.Binary(string="Tài liệu kèm theo")
	attachment_name = fields.Char('Tên tài liệu')
	notification_log_ids = fields.One2many('liy.ydms.notification.log', 'notification_id',
										   string='Nhật kí gửi thông báo')
