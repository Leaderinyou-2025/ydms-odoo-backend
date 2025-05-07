import json
import math

from odoo import http
from odoo.http import request, Response
from . import utils

class ClassroomController(http.Controller):
    @http.route(
        '/api/classrooms/search',
        auth='none',
        type='http',
        cors='*',
        csrf=False,
        methods=['GET'],
    )
    def get_classrooms(self, **kwargs):
        name = kwargs.get('name', '').strip()
        code = kwargs.get('code', '').strip()
        school_id = kwargs.get('school_id', '').strip()
        keyword = kwargs.get('keyword', '').strip()
        page, size, offset = utils._parse_paging(self, kwargs)
        domain = []
        if name:
            domain.append(('name', 'ilike', name))
        if code:
            domain.append(('code', 'ilike', code))
        if school_id:
            domain.append(('school_id', '=', school_id))
        if keyword:
            domain = ['|',
                      ('name', 'ilike', keyword),
                      ('code', 'ilike', keyword)]
        total = request.env['liy.ydms.classroom'].sudo().search_count(domain)

        records = request.env['liy.ydms.classroom'].sudo().search(domain, offset=offset, limit=size, order='id asc')
        items = [{
            'id': c.id,
            'name': c.name,
            'code': c.code,
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
        '/api/classrooms/<int:classroom_id>',
        auth='none',
        type='http',
        cors='*',
        csrf=False,
        methods=['GET'],
    )
    def get_classroom(self, classroom_id, **kwargs):
        try:
            classroom = request.env['liy.ydms.school'].sudo().browse(classroom_id)
            if not classroom.exists():
                return request.make_response(
                    json.dumps({'error': 'Không tìm thấy lớp học với ID %s' % classroom_id}),
                    headers=[('Content-Type', 'application/json')],
                    status=404
                )

            result = {
                'id': classroom.id,
                'name': classroom.name,
                'code': classroom.code,
            }

            return utils._json_response(self, {'success': True, 'data': result})
        except Exception as e:
            return request.make_response(
                json.dumps({'error': str(e)}),
                headers=[('Content-Type', 'application/json')],
                status=500
            )