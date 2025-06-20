{
    'name': 'Records Management',
    'version': '18.0.1.0.0',
    'summary': 'Manage records efficiently within Odoo. Centralized storage, search, permissions, and audit trails.',
    'description': """
Records Management
==================
A comprehensive module for managing records, integrating with stock and web modules.
Features include custom models, views, demo data, and scheduled actions.
""",
    'author': 'John Cope',
    'website': 'https://suncityshred.com',
    'category': 'Tools',
    'license': 'OPL-1',
    'icon': 'records_management/static/description/records_management_icon.png',
    'depends': [
        'base',
        'stock',
        'web',
        'mail',
        'portal',
        'board',
        'product',
        'contacts'
    ],
    'data': [
        'views/inventory_template.xml',
        'views/pickup_request.xml',
        'views/my_portal_inventory.xml',
        'views/shredding_views.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/products.xml',
        'data/scheduled_actions.xml'
    ],
    'installable': True,
    'application': True,
    'live_test_url': 'https://john75suncity-ssh-git-github-com-odoo-odoo-git-8-0--21364046.dev.odoo.com/web/login',
    'price': 2000,
    'currency': 'USD',
    'support': 'john@suncityshred.com'
}