# -*- coding: utf-8 -*-
#############################################################################
#    Copyright (C) 2025 LeaderInYou
#    Author: Oceantech Team
#############################################################################
{
	'name': 'YDMS',
	'version': '1.0.0',
	'category': 'LeaderInYou',
	'summary': 'Youth Development Monitoring System',
	'description': """This initiative aims to address pressing mental health challenges faced by Vietnamese youth aged 10-15 by leveraging advanced digital technology.""",
	'author': "Oceantech Team",
	'company': 'LeaderInYou',
	'maintainer': 'LeaderInYou',
	'live_test_url': '',
	'website': "https://leaderinyou.vn, https://about.leaderinyou.vn",
	'depends': ['base', 'mail'],
	'data': [
		'security/ydms_security.xml',
		'security/ir.model.access.csv',
		'menu/menu.xml',

		# Share Directories
		'views/share_directories/school_views.xml',
		'views/share_directories/classroom_views.xml',
		'views/share_directories/address_views.xml',
		'views/share_directories/avatar_views.xml',

		# Base
		'views/base/partner_views.xml',
		'views/base/users_views.xml',

		# Biz
		'views/category_views.xml',
	],
	'demo': [],
	'images': [],
	'license': 'LGPL-3',
	'installable': True,
	'auto_install': False,
	'application': True,
}
