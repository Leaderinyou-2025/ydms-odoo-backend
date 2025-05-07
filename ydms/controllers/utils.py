import json

from odoo.http import Response


def _json_response(self, data, status=200):
    return Response(
        json.dumps(data, ensure_ascii=False),
        content_type='application/json',
        status=status
    )


def _parse_paging(self, kwargs):
    try:
        page = max(1, int(kwargs.get('page', 1)))
        size = max(1, int(kwargs.get('size', 20)))
    except ValueError:
        page, size = 1, 20
    offset = (page - 1) * size
    return page, size, offset