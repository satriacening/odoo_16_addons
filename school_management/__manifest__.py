# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School',
    'version': '1.0.0',
    'description': """
        This is a addon school management system
        for free
    """,
    'category': 'School',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/student_view.xml',
    ],
    'installable': True,
    'application': True
}
