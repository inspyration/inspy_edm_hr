# -*- coding: utf-8 -*-
##############################################################################
#
#    EDM hr, module for Odoo, Open Source Management Solution
#    Copyright (C) 2014 InsPyration EURL (<http://www.inspyration.fr>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields,osv

class hr(osv.osv):
    _inherit = 'hr.employee'

    def _edm_docs_count(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for employee in self.browse(cr, uid, ids, context=context):
            res[employee.id] = len(employee.document_ids)
        return res

    _columns = {
        'document_ids': fields.one2many(
            'inspy.edm.doc',
            'employee_id',
            string="Documents",
        ),
        'edm_docs_count': fields.function(
            _edm_docs_count,
            string="Documents",
            type='integer',
        ),
    }
