# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSFriend(models.Model):
	_name = "liy.ydms.friend"
	_description = u'Bạn bè của học sinh'
	_inherit = ['mail.thread']
	_order = 'name desc'

	friend_id = fields.Many2one('res.users', string=u'Bạn', required=True)
	name = fields.Char(string=u'Tên người bạn', related='friend_id.name')
	avatar = fields.Image(string=u'Hình đại diện', related='friend_id.avatar_1920')
	nickname = fields.Char(string=u'Biệt danh', related='friend_id.partner_id.nickname')
	friendly_point = fields.Integer(string=u'Điểm thân thiện', default=0)
	status = fields.Selection([
		('new', u'Lời mời kết bạn'),
		('accepted', u'Đồng ý'),
		('cancel', u'Không đồng ý')
	], string=u'Trạng thái', default='new', required=True)
	user_id = fields.Many2one('res.users', string=u'Học sinh', required=True)

	@api.model_create_multi
	def create(self, vals_list):
		if not isinstance(vals_list, list):
			vals_list = [vals_list]

		records = super(YDMSFriend, self).create(vals_list)
		if not self._context.get('is_reciprocal'):  # Kiểm tra để tránh lặp vô hạn
			for record in records:
				# Đặt trạng thái của bản ghi hiện tại là accepted
				record.status = 'accepted'
				# Tạo bản ghi đối ứng cho người bạn
				self.with_context(is_reciprocal=True).create([{
					'user_id': record.friend_id.id,
					'friend_id': record.user_id.id,
					'status': 'new',
					'friendly_point': 0,
				}])
		return records

	def write(self, vals):
		if self._context.get('skip_reciprocal_update'):
			return super(YDMSFriend, self).write(vals)

		if 'status' in vals and any(record.status == 'accepted' for record in self):
			raise UserError(u'Không thể sửa trạng thái. Vui lòng xóa bản ghi để hủy kết bạn.')

		# Kiểm tra trước khi cập nhật
		if 'status' in vals and vals['status'] == 'accepted':
			for record in self:
				if record.status != 'new':
					continue
				reciprocal = self.env['liy.ydms.friend'].search([
					('user_id', '=', record.friend_id.id),
					('friend_id', '=', record.user_id.id),
				], limit=1)
				if reciprocal:
					self.env['liy.ydms.friend'].with_context(skip_reciprocal_update=True).browse([
						record.id, reciprocal.id
					]).write({
						'friendly_point': record.friendly_point + 5,
						'status': 'accepted'
					})
		res = super(YDMSFriend, self).write(vals)
		if 'status' in vals and vals['status'] == 'cancel':
			for record in self:
				reciprocal = self.env['liy.ydms.friend'].search([
					('user_id', '=', record.friend_id.id),
					('friend_id', '=', record.user_id.id),
				], limit=1)
				if reciprocal:
					reciprocal.with_context(skip_reciprocal_update=True).write({
						'status': 'cancel'
					})
		return res

	def unlink(self):
		if self._context.get('skip_reciprocal_unlink'):
			return super(YDMSFriend, self).unlink()

		for record in self:
			reciprocal = self.env['liy.ydms.friend'].search([
				('user_id', '=', record.friend_id.id),
				('friend_id', '=', record.user_id.id),
			])
			if reciprocal:
				reciprocal.with_context(skip_reciprocal_unlink=True).unlink()
		return super(YDMSFriend, self).unlink()

	@api.constrains('user_id', 'friend_id')
	def _check_unique_friendship(self):
		"""Kiểm tra không tạo trùng lặp quan hệ bạn bè."""
		for record in self:
			duplicate = self.env['liy.ydms.friend'].search([
				('user_id', '=', record.user_id.id),
				('friend_id', '=', record.friend_id.id),
				('id', '!=', record.id),
			])
			if duplicate:
				raise ValidationError(u'Quan hệ bạn bè giữa hai người dùng này đã tồn tại!')
