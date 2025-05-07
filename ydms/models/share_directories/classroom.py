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
    school_id = fields.Many2one(string=u'Trường', tracking=True)

