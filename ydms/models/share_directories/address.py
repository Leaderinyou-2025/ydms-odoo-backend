# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


# Tỉnh thành - inherit country state
class YDMSCountryState(models.Model):
	_description = u"Tỉnh thành"
	_inherit = 'res.country.state'
	_order = 'name'

	admin_code = fields.Char(u'Mã hành chính')
	district_ids = fields.One2many('liy.ydms.district', 'state_id', u'Quận huyện')
	precint_ids = fields.One2many('liy.ydms.precint', 'state_id', u'Phường xã')
	order_weight = fields.Integer(string=u'Thứ tự hiển thị', default=1)


# Quận huyện
class YDMSDistrict(models.Model):
	_name = 'liy.ydms.district'
	_description = u"Quận huyện"
	_order = 'name'

	# Master fields
	state_id = fields.Many2one('res.country.state', string=u'Tỉnh thành', required=True)

	name = fields.Char(u'Tên Quận huyện', required=True)
	admin_code = fields.Char(u'Mã hành chính')
	precint_ids = fields.One2many('liy.ydms.precint', 'district_id', u'Quận huyện')
	order_weight = fields.Integer(string=u'Thứ tự hiển thị', default=1)


# Xã phường
class YDMSPrecint(models.Model):
	_name = 'liy.ydms.precint'
	_description = u"Xã phường"
	_order = 'name'

	# Master fields
	state_id = fields.Many2one('res.country.state', string=u'Tỉnh thành', required=True)
	district_id = fields.Many2one('liy.ydms.district', string=u'Quận huyện')

	name = fields.Char(u'Tên Phường xã', required=True)
	admin_code = fields.Char(u'Mã hành chính')
	order_weight = fields.Integer(string=u'Thứ tự hiển thị', default=1)


class HostopiaAddressMixin(models.AbstractModel):
	_inherit = 'format.address.mixin'
	_description = 'YDMS Address Mixin'

	@api.onchange('precint_id')
	def _onchange_precint_id(self):
		if self.precint_id.district_id:
			self.district_id = self.precint_id.district_id
		if self.precint_id.state_id:
			self.state_id = self.precint_id.state_id

	@api.onchange('district_id')
	def _onchange_district_id(self):
		if self.district_id.state_id:
			self.state_id = self.district_id.state_id
		if (not self.district_id) or (self.precint_id.district_id != self.district_id):
			self.precint_id = False

	@api.onchange('state_id')
	def _onchange_state_id(self):
		if self.state_id.country_id:
			self.country_id = self.state_id.country_id
		if (not self.state_id) or (self.district_id.state_id != self.state_id):
			self.district_id = False

	@api.model
	def _get_default_country_id(self):
		country = self.env['res.country'].search([('phone_code', '=', 84)], limit=1)
		return country and country.id or False

	country_id = fields.Many2one('res.country', string=u'Quốc gia', default=_get_default_country_id)
	precint_id = fields.Many2one('liy.ydms.precint', string=u'Phường xã', domain="[('state_id', '=?', state_id)]")
	district_id = fields.Many2one('liy.ydms.district', string=u'Quận huyện', domain="[('state_id', '=?', state_id)]")
	is_address = fields.Boolean(u'Là địa chỉ')
