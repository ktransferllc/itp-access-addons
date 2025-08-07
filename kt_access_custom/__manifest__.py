# -*- coding: utf-8 -*-
#################################################################################
# Author      : Knowledge Transfer LLC
# License     : Odoo Proprietary License v1.0
#
#################################################################################
{
    "name": "KT Access Custom",
    "summary": "Implementation of saas for KT",
    "category": "Hidden",
    "version": "1.0.0",
    "author": "Knowledge Transfer LLC",
    "maintainer": "Anderson David Martinez",
    "email": "david@knowledgetransferllc.com",
    "website": "https://www.knowledgetransferllc.com",
    "description": """Implementation of saas for KT""",
    "depends": [
        'base',
        'saas_cluster_simple',
    ],
    "data": [
    ],
    "images": ['static/description/logo.png'],
    'qweb': [
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    "currency": 'USD',
    "license":  "OPL-1",
}