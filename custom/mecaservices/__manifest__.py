# -*- coding: utf-8 -*-
{
    "name": "mecaservices",
    "summary": "Application de gestion d'ordre de réparation de mécanique agricole.",
    "description": """
Cette application permet de gérer les ordres de réparations et les parcs de machines des clients.
    """,
    "author": "Benjamin Gras",
    "website": "https://www.mecaservices57.fr",
    "application": True,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
