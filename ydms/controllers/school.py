import json
import math

from odoo import http
from odoo.http import request, Response
from . import utils

class ClassroomController(http.Controller):
    @http.route(
        '/api/schools/search',
        auth='none',
        type='http',
        cors='*',
        csrf=False,
        methods=['GET'],
    )
    def get_schools(self, **kwargs):
        name = kwargs.get('name', '').strip()
        code = kwargs.get('code', '').strip()
        keyword = kwargs.get('keyword', '').strip()
        page, size, offset = utils._parse_paging(self, kwargs)
        domain = []
        domain.append(('is_school', '=', True))
        if name:
            domain.append(('name', 'ilike', name))
        if code:
            domain.append(('code', 'ilike', code))
        if keyword:
            domain = ['|',
                      ('name', 'ilike', keyword),
                      ('code', 'ilike', keyword)]
        total = request.env['res.partner'].sudo().search_count(domain)

        records = request.env['res.partner'].sudo().search(domain, offset=offset, limit=size, order='id asc')
        items = [{
            'id': c.id,
            'name': c.name,
            'code': c.code,
            'image1920': c.image_1920.decode('utf-8') if c.image_1920 else None,
        } for c in records]

        # Tính tổng số trang
        total_pages = math.ceil(total / size) if total else 0

        result = {
            'success': True,
            'page': page,
            'size': size,
            'total': total,
            'totalPages': total_pages,
            'data': items,
        }
        return utils._json_response(self, result)

    @http.route(
        '/api/schools/<int:id>',
        auth='none',
        type='http',
        cors='*',
        csrf=False,
        methods=['GET'],
    )
    def get_school(self, id, **kwargs):
        try:
            school = request.env['res.partner'].sudo().browse(id)
            if not school.exists():
                return utils._json_response(self, {'error': 'Không tìm thấy trường học với ID %s' % id}, status=404)
            classrooms = [{
                'id': c.id,
                'name': c.name,
            } for c in school.classroom_ids]

            result = {
                'id': school.id,
                'name': school.name,
                'code': school.code,
                'classrooms': classrooms,
                'image1920': school.image_1920.decode('utf-8') if school.image_1920 else None,
            }

            return utils._json_response(self, {'success': True, 'data': result})
        except Exception as e:
            return utils._json_response(self, {'error': str(e)}, status=500)