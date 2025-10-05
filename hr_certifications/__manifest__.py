# -*- coding: utf-8 -*-
#############################################################################
#
#    Author: Nandakishore M(<https://nandakishore.odoo.com/>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'HR Certifications',
    'version': '18.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Track employee certifications',
    'description': """This module adds employee certification tracking to 
    Odoo HR""",
    'maintainer': 'Nandakishore M',
    'company': 'Nandakishore M',
    'website': 'https://nandakishore.odoo.com/',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/hr_certification_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
