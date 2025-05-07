from odoo import http
from odoo.http import request
from . import utils


class AddressController(http.Controller):

    @http.route(
        '/api/address/states',
        auth='none',
        type='http',
        cors='*',
        csrf=False,
        methods=['GET'],
    )
    def get_states(self, **kwargs):
        name = kwargs.get('name', '').strip()
        keyword = kwargs.get('keyword', '').strip()
        page, size, offset = utils._parse_paging(self, kwargs)

        domain = []
        if name:
            domain.append(('name', 'ilike', name))
        if keyword:
            domain = ['|',
                      ('name', 'ilike', keyword),
                      ('code', 'ilike', keyword),
                      ('admin_code', 'ilike', keyword)]
        model = request.env['res.country.state'].sudo()
        total = model.search_count(domain)
        states = model.search(domain, offset=offset, limit=size, order='order_weight asc, name asc')

        return utils._json_response(self, {
            'page': page,
            'size': size,
            'total': total,
            'data': [{
                'id': s.id,
                'name': s.name,
                'code': s.code,
                'admin_code': s.admin_code
            } for s in states]
        })

    @http.route(
        '/api/address/districts',
        auth='none',
        type='http',
        cors='*',
        csrf=False,
        methods=['GET'],
    )
    def get_districts(self, **kwargs):
        state_id = kwargs.get('state_id')
        name = kwargs.get('name', '').strip()
        keyword = kwargs.get('keyword', '').strip()
        page, size, offset = utils._parse_paging(self, kwargs)

        domain = []
        if state_id:
            domain.append(('state_id', '=', int(state_id)))
        if name:
            domain.append(('name', 'ilike', name))
        if keyword:
            domain = ['|',
                      ('name', 'ilike', keyword),
                      ('admin_code', 'ilike', keyword)]

        model = request.env['liy.ydms.district'].sudo()
        total = model.search_count(domain)
        districts = model.search(domain, offset=offset, limit=size, order='order_weight asc, name asc')

        return utils._json_response(self, {
            'page': page,
            'size': size,
            'total': total,
            'data': [{
                'id': d.id,
                'name': d.name,
                'state_id': d.state_id.id,
                'state_name': d.state_id.name,
                'admin_code': d.admin_code,
            } for d in districts]
        })

    @http.route(
        '/api/address/precints',
        auth='none',
        type='http',
        cors='*',
        csrf=False,
        methods=['GET'],
    )
    def get_precints(self, **kwargs):
        state_id = kwargs.get('state_id')
        district_id = kwargs.get('district_id')
        name = kwargs.get('name', '').strip()
        keyword = kwargs.get('keyword', '').strip()
        page, size, offset = utils._parse_paging(self, kwargs)

        domain = []
        if state_id:
            domain.append(('state_id', '=', int(state_id)))
        if district_id:
            domain.append(('district_id', '=', int(district_id)))
        if name:
            domain.append(('name', 'ilike', name))
        if keyword:
            domain = ['|',
                      ('name', 'ilike', keyword),
                      ('admin_code', 'ilike', keyword)]

        model = request.env['liy.ydms.precint'].sudo()
        total = model.search_count(domain)
        precints = model.search(domain, offset=offset, limit=size, order='order_weight asc, name asc')

        return utils._json_response(self, {
            'page': page,
            'size': size,
            'total': total,
            'data': [{
                'id': p.id,
                'name': p.name,
                'state_id': p.state_id.id,
                'state_name': p.state_id.name,
                'district_id': p.district_id.id if p.district_id else None,
                'district_name': p.district_id.name if p.district_id else None,
                'admin_code': p.admin_code
            } for p in precints]
        })
