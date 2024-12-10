{
    'name':'Device Managementt',
    'author':'rituraj',
    'depends':['base','hr'],
    'installable': True,
    'application': True,
    'data':[
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/device_assignment_views.xml',
        'views/device_attribute_views.xml',
        'views/device_brand_views.xml',
        'views/device_model.xml',
        'views/device_views.xml',
        'views/menu.xml',
        'views/device_attribute_assignment_view.xml'
    ],
'translations': [
        'i18n/device_model.hindi.po',
        'i18n/device_model.italian.po'
    ]
}