# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSSchool(models.Model):
	_description = u'Trường học'
	_inherit = ['res.partner']
	_order = 'name asc'

	name = fields.Char(string=u'Tên trường', required=True, tracking=True)
	code = fields.Char(string=u'Mã trường', tracking=True)
	is_school = fields.Boolean(u'Trường học', default = False, tracking=True)
	classroom_ids = fields.One2many('liy.ydms.classroom', 'school_id', string='Danh sách lớp học')

	_sql_constraints = [
		('unique_school_name', 'unique(name)', 'Tên trường đã tồn tại!'),
		('unique_school_code', 'unique(code)', 'Mã trường đã tồn tại!'),
	]

	def unlink(self):
		for record in self:
			if record.is_school:
				# Check lớp học liên kết
				if record.classroom_ids:
					raise UserError(f"Không thể xóa trường '{record.name}' vì đã có lớp học liên kết.")
				# Check người dùng liên quan
				user_exists = self.env['res.users'].search_count([('school_id', '=', record.id)])
				if user_exists:
					raise UserError(f"Không thể xóa trường '{record.name}' vì đã có tài khoản người dùng liên kết.")
		# Nếu không có ràng buộc, cho phép xóa
		return super().unlink()