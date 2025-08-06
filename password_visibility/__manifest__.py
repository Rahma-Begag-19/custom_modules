# __manifest__.py
{
    'name': 'Password Visibility Toggle',
    'version': '17.0.1.0.0',
    'category': 'Website',
    'summary': 'Adds a password visibility toggle button to the Odoo login page',
    'description': """
        This module adds an eye icon to the Odoo 17 login page, allowing users to toggle password visibility.
    """,
    'author': 'Rahma BEGAG',
    'website': 'https://www.linkedin.com/in/rahma-begag-b49a70349/',
    'license': 'LGPL-3',
    'depends': ['web', 'auth_signup'],
    'data': [
        'views/web_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
