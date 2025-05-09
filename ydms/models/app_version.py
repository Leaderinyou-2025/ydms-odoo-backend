# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSAppVersion(models.Model):
	_name = 'liy.ydms.app.version'
	_description = u'Quản lý phiên bản App'
	_inherit = ['mail.thread']
	_order = 'name desc'

	name = fields.Char(string=u'Version name', required=True)
	version_build = fields.Char(string=u'Version build')
	version_code = fields.Char(string=u'Version code')
	desciption = fields.Char(string=u'Description')
	platform = fields.Selection([
		('ios', 'iOS'),
		('android', 'Android'),
	], default='ios', string=u'Platform', required=True)
	build_bundle_file = fields.Binary(string=u'App Bundle id', attachment=True)
	public_url = fields.Char(string=u'Download URL')
	active = fields.Boolean(u'Active', default = True)


