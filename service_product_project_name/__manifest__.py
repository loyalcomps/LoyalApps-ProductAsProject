# -*- coding: utf-8 -*-
{
    'name': "service_product_project_name",

    'summary': """
        Change the project name according to the service product""",

    'description': """
       Project name as service tracking 
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "https://www.loyalitsolutions.com",
    'maintainer': "Loyal IT Solutions",
    'category': 'Point of Sale',
    'version': '16.0.1.0.0',
    # any module necessary for this one to work correctly
    'depends': ['base','sale_project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/banner.png'],
}
