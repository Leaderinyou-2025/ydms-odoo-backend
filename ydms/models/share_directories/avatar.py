# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError

class YDMSAvatar(models.Model):
	_name = 'liy.ydms.avatar'
	_description = u'Thư viện hình đại diện'
	_inherit = ['image.mixin']
	_order = 'name asc'

	name = fields.Char(string=u'Tên hình đại diện', required=True)
	tags = fields.Char(string=u'Từ khoá', required=True)
