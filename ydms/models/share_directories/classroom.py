# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSClassroom(models.Model):
    _name = "liy.ydms.classroom"
    _description = u'Lớp học'
    _inherit = ['mail.thread']
    _order = 'name desc'

    name = fields.Char(string=u'Tên lớp', required=True, tracking=True)
    code = fields.Char(string=u'Mã lớp', tracking=True)
    school_id = fields.Many2one('res.partner', string=u'Trường', tracking=True)

    _sql_constraints = [
        ('unique_classroom_name', 'unique(name, school_id)', 'Tên lớp đã tồn tại!'),
        ('unique_classroom_code', 'unique(code, school_id)', 'Mã lớp đã tồn tại!'),
    ]

    def unlink(self):
        for record in self:
            # Check người dùng liên quan
            user_exists = self.env['res.users'].search_count([('classroom_id', '=', record.id)])
            if user_exists:
                raise UserError(f"Không thể xóa lớp '{record.name}' vì đã có tài khoản người dùng liên kết.")
        # Nếu không có ràng buộc, cho phép xóa
        return super().unlink()
