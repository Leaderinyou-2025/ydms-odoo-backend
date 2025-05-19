# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
import math

from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSEmotionalQuestion(models.Model):
	_name = 'liy.ydms.emotional.question'
	_description = u'Câu hỏi cảm xúc'
	_order = 'name desc'

	name = fields.Char(string=u'Câu hỏi', required=True)
	encourage_interaction = fields.Char(string=u'Câu khuyến khích tương tác')
	answer_ids = fields.One2many('liy.ydms.emotional.answer.option', 'question_id', string=u'Các phương án trả lời')
	rank_point = fields.Integer(string=u'Điểm thưởng xếp hạng')

	@api.model
	def get_list(self, record_per_page=1000, page_num=1, **kwargs):
		name = kwargs.get('name', '').strip()
		keyword = kwargs.get('keyword', '').strip()
		page_num = max(1, page_num)
		offset = (page_num - 1) * record_per_page
		domain = []
		if name:
			domain.append(('name', 'ilike', name))
		if keyword:
			domain += ['|',
					   ('name', 'ilike', keyword),
					   ('encourage_interaction', 'ilike', keyword)]
		total = self.env['liy.ydms.emotional.question'].search_count(domain)
		records = self.env['liy.ydms.emotional.question'].search(domain, offset=offset, limit=record_per_page, order='id desc')

		items = [{
			'id': c.id,
			'name': c.name,
			'encourage_interaction': c.encourage_interaction,
			'answer_ids': [{'id': a.id, 'name': a.name} for a in c.answer_ids],
			'rank_point': c.rank_point,
		} for c in records]
		# Tính tổng số trang
		total_pages = math.ceil(total / record_per_page) if total else 0
		# Trả về kết quả
		return {
			'status_code': 200,
			'data': items,
			'message': None,
			'page': page_num,
			'size': record_per_page,
			'total': total,
			'totalPages': total_pages,
		}

	@api.model
	def get_detail(self, id):
		if not id:
			return {
				'status_code': 400,
				'message': u'Missing ID',
			}
		record = self.env['liy.ydms.emotional.question'].browse(id)
		if not record.exists():
			return {
				'status_code': 404,
				'message': u'Không tìm thấy câu hỏi cảm xúc với ID %s' % id,
			}
		items = {
			'id': record.id,
			'name': record.name,
			'encourage_interaction': record.encourage_interaction,
			'answer_ids': [{'id': a.id, 'name': a.name} for a in record.answer_ids],
			'rank_point': record.rank_point,
		}
		return {
			'status_code': 200,
			'data': items,
			'message': None
		}

	@api.model
	def create_model(self, vals):
		if not vals.get('name'):
			return {
				'status_code': 400,
				'message': u'Tên câu hỏi không được để trống',
			}
		try:
			record = self.create(vals)
			return {
				'status_code': 200,
				'data': record.id,
				'message': u'Tạo mới câu hỏi cảm xúc thành công'
			}
		except ImportValidationError as e:
			return {
				'status_code': 400,
				'message': str(e),
			}

	@api.model
	def write_model(self, vals):
		if not vals.get('name'):
			return {
				'status_code': 400,
				'message': u'Tên câu hỏi không được để trống',
			}
		try:
			record = self.write(vals)
			return {
				'status_code': 200,
				'data': record.id,
				'message': u'Cập nhật câu hỏi cảm xúc thành công'
			}
		except ImportValidationError as e:
			return {
				'status_code': 400,
				'message': str(e),
			}

	@api.model
	def delete(self, id):
		if not id:
			return {
				'status_code': 400,
				'message': u'Missing ID',
			}
		record = self.browse(id)
		if not record.exists():
			return {
				'status_code': 404,
				'message': u'Không tìm thấy câu hỏi cảm xúc với ID %s' % id,
			}
		try:
			record.answer_ids.unlink()
			record.unlink()
			return {
				'status_code': 200,
				'message': u'Xóa câu hỏi cảm xúc thành công'
			}
		except UserError as e:
			return {
				'status_code': 400,
				'message': str(e),
			}