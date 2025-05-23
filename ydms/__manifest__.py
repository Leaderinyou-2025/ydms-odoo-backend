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

		# Integrate
		'views/integrate/fcm_notification_views.xml',
		'views/integrate/fcm_notification_log_views.xml',

		# Biz
		'views/category_views.xml',
		'views/app_version_views.xml',
		'views/emotional_question_views.xml',
		'views/emotional_answer_option_views.xml',
		'views/emotional_diary_views.xml',
		'views/assessment_answer_option_views.xml',
		'views/assessment_question_views.xml',
		'views/assessment_views.xml',
		'views/guide_views.xml',
		'views/badge_views.xml',
		'views/leaderboard_views.xml',
		'views/achievement_views.xml',
		'views/experience_views.xml',
		'views/experience_review_views.xml',

		'views/task_views.xml',
		'views/assessment_answer_result_views.xml',
		'views/assessment_result_views.xml',
		'views/friend_views.xml',
	],
    'assets': {
        'web.assets_backend': [
            'ydms/static/css/img.css',
        ],
    },
    'demo': [],
    'images': [],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
