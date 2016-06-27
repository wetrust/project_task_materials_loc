# -*- coding: utf-8 -*-
# (c) 2016 Nueva Gestión - Jonathan Gutiérrez
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Project Task Materials Location',
    'summary': 'Permite seleccionar ubicación para un material de una tarea de un proyecto',
    'version': '0.1',
    'category': "Project Management",
    'author': u'Nueva Gestión',
    'website': 'http://nuevagestion.cl',
    'license': 'AGPL-3',
    'depends': ['project_task_materials', 'project_task_materials_stock', 'stock'],
    'data': [
        'views/project_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
