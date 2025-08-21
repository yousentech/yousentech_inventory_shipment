
{
    'name': 'yousentech_inventory_shipment',
    'category': 'Inventory',
    'summary': """.""",
    'description': """""",
    'author': 'yousen tech Techno Solutions, Odoo SA',
    'website': "https://www.qimamhd.com",
    'company': 'yousen Techno Solutions',
    'maintainer': 'yousen Techno Solutions',
    'depends': ['base','stock','yousentech_inventory'],
    'data': [
        'security/security.xml',
        'views/stock_move.xml',
        'views/stock_picking.xml'
    ],
  
    'images': ['static/description/icon.png'],

    'license': 'LGPL-3',
    'images': [],
    'sequence': '-100',
    'installable': True,
    'auto_install': False,
    'application': True,
}
