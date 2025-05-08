from odoo import http
from odoo.http import request
from . import utils


class AvatarController(http.Controller):
    @http.route(
        '/api/avatar/<int:id>',
        auth='none',
        type='http',
        cors='*',
        csrf=False,
        methods=['GET'],
    )
    def get_avatar(self, id, **kwargs):
        entity = request.env['liy.ydms.avatars'].sudo().browse(id)
        if not entity.exists():
            return utils._json_response(self, {'error': 'Không tìm thấy Avatar'}, status=404)
        return utils._json_response(self, {
            'id': entity.id,
            'name': entity.name,
            'image': entity.image_1920.decode('utf-8') if entity.image_1920 else None,
            'tags': entity.tags,
        })


