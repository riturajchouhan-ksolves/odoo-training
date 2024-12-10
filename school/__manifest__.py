{
    'name':'Odoo School',
    'author':'rituraj',
    'depends':['base'],
    'installable':True,
    'application':True,
    'auto_install':False,
    'data':[
            'security/ir.model.access.csv',
            # 'security/record_rules.xml',
            'views/student_views.xml',
            'views/subject_views.xml',
            'views/class_views.xml',
            'views/fee_view.xml',
            'views/exam_views.xml',
            'views/exam_wizard_views.xml',
            'reports/exam_report.xml',
            'reports/report_action.xml',
            'views/menu.xml',

    ]

}