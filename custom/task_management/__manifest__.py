
{
    'name': 'Management Tasks',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Allows you to create and assign tasks, track progress and receive notifications when tasks are completed',
    'description': """
    This module allows users to create and assign tasks, track progress and receive notifications when tasks are completed.
    """,
    'author': 'Mario Riascos',
    'website': 'https://mfriascos.github.io/mfriascos1',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/tasks_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
