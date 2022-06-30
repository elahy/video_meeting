# -*- coding: utf-8 -*-

{
    'name': 'Video Meetings',
    'version': '1.0.0',
    'category': 'Meetings',
    'author': 'Qudrat-E-Elahy',
    'sequence': -120,
    'summary': 'Live Video Chat and Meetings',
    'description': """Live Video Chat and Meetings""",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/participant_view.xml',
        'views/channel_view.xml',
        'views/configuration_view.xml',
        'views/meeting_view.xml',
        'views/meeting_tag_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},
    'post_init_hook': '',
    'license': 'LGPL-3',
}
