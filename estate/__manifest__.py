{
    'name':'Estate Property',
    'depends':['base','mail'],
    'installable':True,
    'application':True,
    'auto_install':False,
    'data':[
            "security/security.xml",
            "security/ir.model.access.csv",
            "views/estate_view.xml",
            "views/ir_cron_data.xml"
    ]
}