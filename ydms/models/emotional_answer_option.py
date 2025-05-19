# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
import math

from odoo import api, fields, models, tools, _
from odoo.addons.base_import.models.base_import import ImportValidationError
from odoo.exceptions import UserError, ValidationError


class YDMSEmotionalAnswerOption(models.Model):
    _name = 'liy.ydms.emotional.answer.option'
    _description = u'Câu hỏi cảm xúc - Các phương án trả lời câu hỏi'
    _inherit = ['image.mixin']
    _order = 'question_id, order_weight'

    # Master field
    question_id = fields.Many2one('liy.ydms.emotional.question', string=u'Câu hỏi', required=True)

    # Data fields
    name = fields.Char(string=u'Câu trả lời', required=True)
    scores = fields.Integer(string=u'Điểm chuyên môn', required=True)
    encourage = fields.Html(string=u'Câu động viên')
    guide_category_ids = fields.Many2many('liy.ydms.category', string=u'Hướng dẫn điều tiết cảm xúc')
    order_weight = fields.Integer(string=u'Thứ tự hiển thị', default=1)

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
                       ('encourage', 'ilike', keyword)]
        total = self.env['liy.ydms.emotional.answer.option'].search_count(domain)
        records = self.env['liy.ydms.emotional.answer.option'].search(domain, offset=offset, limit=record_per_page,
                                                                     order='question_id, order_weight asc')

        items = [{
            'id': c.id,
            'name': c.name,
            'scores': c.scores,
            'encourage': c.encourage,
            'guide_category_ids': [{'id': a.id, 'name': a.name} for a in c.guide_category_ids],
            'order_weight': c.order_weight,
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
        record = self.env['liy.ydms.emotional.answer.option'].browse(id)
        if not record.exists():
            return {
                'status_code': 404,
                'message': u'Không tìm thấy bản ghi với ID %s' % id,
            }
        return {
            'status_code': 200,
            'data': {
                'id': record.id,
                'name': record.name,
                'scores': record.scores,
                'encourage': record.encourage,
                'guide_category_ids': [{'id': a.id, 'name': a.name} for a in record.guide_category_ids],
                'order_weight': record.order_weight,
            },
            'message': None,
        }

    @api.model
    def create_model(self, vals):
        if not vals.get('name'):
            return {
                'status_code': 400,
                'message': u'Missing name',
            }
        if not vals.get('question_id'):
            return {
                'status_code': 400,
                'message': u'Missing question_id',
            }
        if not vals.get('scores'):
            return {
                'status_code': 400,
                'message': u'Missing scores',
            }
        record = self.create(vals)
        return {
            'status_code': 200,
            'data': {
                'id': record.id,
                'name': record.name,
                'scores': record.scores,
                'encourage': record.encourage,
                'guide_category_ids': [{'id': a.id, 'name': a.name} for a in record.guide_category_ids],
                'order_weight': record.order_weight,
            },
            'message': None
        }

    @api.model
    def write_model(self, vals):
        if not vals.get('name'):
            return {
                'status_code': 400,
                'message': u'Missing name',
            }
        if not vals.get('question_id'):
            return {
                'status_code': 400,
                'message': u'Missing question_id',
            }
        if not vals.get('scores'):
            return {
                'status_code': 400,
                'message': u'Missing scores',
            }
        record = self.write(vals)
        return {
            'status_code': 200,
            'data': {
                'id': record.id,
                'name': record.name,
                'scores': record.scores,
                'encourage': record.encourage,
                'guide_category_ids': [{'id': a.id, 'name': a.name} for a in record.guide_category_ids],
                'order_weight': record.order_weight,
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
        record = self.browse(id)
        if not record.exists():
            return {
                'status_code': 404,
                'message': u'Không tìm thấy bản ghi với ID %s' % id,
            }
        record.unlink()
        return {
            'status_code': 200,
            'message': u'Xóa bản ghi thành công',
        }