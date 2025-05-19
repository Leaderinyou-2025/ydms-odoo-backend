# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSEmotionalDiary(models.Model):
	_name = 'liy.ydms.emotional.diary'
	_description = u'Nhật ký cảm xúc'
	_inherit = ['mail.thread']
	_order = 'create_date desc'

	teenager_id = fields.Many2one('res.users', string=u'Học sinh', required=True)
	nickname = fields.Char(related='teenager_id.partner_id.nickname')
	question_id = fields.Many2one('liy.ydms.emotional.question', string=u'Câu hỏi', required=True)
	answer_id = fields.Many2one('liy.ydms.emotional.answer.option', string=u'Câu trả lời')

	answer_text = fields.Char(string=u'Nội dung trả lời', related='answer_id.name')
	answer_icon = fields.Image(string=u'Biểu tượng trả lời', related='answer_id.image_1920')
	rank_point = fields.Integer(related='question_id.rank_point')
	scores = fields.Integer(related='answer_id.scores')

	@api.model
	def get_list(self, record_per_page=1000, page_num=1, **kwargs):
		name = kwargs.get('name', '').strip()
		teenager_id = kwargs.get('teenager_id', None)
		page_num = max(1, page_num)
		offset = (page_num - 1) * record_per_page
		domain = []
		if name:
			domain.append(('name', 'ilike', name))
		if teenager_id:
			domain.append(('teenager_id', '=', teenager_id))
		total = self.env['liy.ydms.emotional.diary'].search_count(domain)
		records = self.env['liy.ydms.emotional.diary'].search(domain, offset=offset, limit=record_per_page, order='id desc')

		items = [{
			'id': c.id,
			'teenager_id': c.teenager_id.id,
			'question_id': c.question_id.id,
			'answer_id': c.answer_id.id,
			'answer_text': c.answer_text,
			'answer_icon': c.answer_icon,
			'rank_point': c.rank_point,
			'scores': c.scores,
			'create_date': c.create_date,
			'nickname': c.nickname,
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
		record = self.env['liy.ydms.emotional.diary'].browse(id)
		if not record.exists():
			return {
				'status_code': 404,
				'message': u'Không tìm thấy nhật ký cảm xúc với ID %s' % id,
			}
		return {
			'status_code': 200,
			'data': {
				'id': record.id,
				'teenager_id': record.teenager_id.id,
				'question_id': record.question_id.id,
				'answer_id': record.answer_id.id,
				'answer_text': record.answer_text,
				'answer_icon': record.answer_icon,
				'rank_point': record.rank_point,
				'scores': record.scores,
				'nickname': record.nickname,
			},
			'message': None
		}

	@api.model
	def create_model(self, vals):
		if not vals.get('teenager_id'):
			return {
				'status_code': 400,
				'message': u'Missing teenager_id',
			}
		if not vals.get('question_id'):
			return {
				'status_code': 400,
				'message': u'Missing question_id',
			}
		if not vals.get('answer_id'):
			return {
				'status_code': 400,
				'message': u'Missing answer_id',
			}
		record = self.env['liy.ydms.emotional.diary'].create(vals)
		return {
			'status_code': 200,
			'data': {
				'id': record.id,
				'teenager_id': record.teenager_id.id,
				'question_id': record.question_id.id,
				'answer_id': record.answer_id.id,
				'answer_text': record.answer_text,
				'answer_icon': record.answer_icon,
				'rank_point': record.rank_point,
				'scores': record.scores,
				'nickname': record.nickname,
			},
			'message': None
		}

	@api.model
	def write_model(self, vals):
		if not vals.get('teenager_id'):
			return {
				'status_code': 400,
				'message': u'Missing teenager_id',
			}
		if not vals.get('question_id'):
			return {
				'status_code': 400,
				'message': u'Missing question_id',
			}
		if not vals.get('answer_id'):
			return {
				'status_code': 400,
				'message': u'Missing answer_id',
			}
		record = self.env['liy.ydms.emotional.diary'].write(vals)
		return {
			'status_code': 200,
			'data': {
				'id': record.id,
				'teenager_id': record.teenager_id.id,
				'question_id': record.question_id.id,
				'answer_id': record.answer_id.id,
				'answer_text': record.answer_text,
				'answer_icon': record.answer_icon,
				'rank_point': record.rank_point,
				'scores': record.scores,
				'nickname': record.nickname,
			},
			'message': None
		}

	@api.model
	def delete(self, id):
		if not id:
			return {
				'status_code': 400,
				'message': u'Missing ID',
			}
		record = self.env['liy.ydms.emotional.diary'].browse(id)
		if not record.exists():
			return {
				'status_code': 404,
				'message': u'Không tìm thấy nhật ký cảm xúc với ID %s' % id,
			}
		record.unlink()
		return {
			'status_code': 200,
			'message': u'Xóa nhật ký cảm xúc thành công',
		}
