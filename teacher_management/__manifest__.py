{
    'name':'Teacher Management',
    'author':'rituraj',
    'version':'1.0',
    'depends':['base','hr','school'],
    'data':[
            'security/ir.model.access.csv',
            'views/class_views.xml',
            'views/teacher_views.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True
}