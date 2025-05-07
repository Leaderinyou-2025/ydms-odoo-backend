# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError

class YDMSSchool(models.Model):
    _name = "liy.ydms.school"
    _description = u'Trường học'
    _inherit = ['res.partner']
    _order = 'name desc'

    name = fields.Char(string=u'Tên trường', required=True, tracking=True)
    code = fields.Char(string=u'Mã trường', required=True, tracking=True)
    classroom_ids = fields.One2many('liy.ydms.classroom', 'school_id', string='Danh sách lớp học')
