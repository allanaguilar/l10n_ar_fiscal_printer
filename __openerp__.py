# -*- coding: utf-8 -*-
##############################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{

'name' : 'Fiscal Printer Manager Argentina',	
'version' : '1.0',
'author' : 'OPENPYME S.R.L',
'category' : 'Fiscal Printers',
'description' : """

FISCAL PRINTER MANAGER
=====================================
Desarrollado actualmente para impresoras Hasar por medio de conexion TCP/IP 
y uso de spooler.

* Multiples impresoras fiscales
* Cola de impresion
* Impresora fiscal relacionada a puntos de venta (l10n_ar_point_of_sale - Proyecto Aconcagua)
* Impresion fiscal remota
* Impresion de Facturas

* TODO - Impresion de remitos
* TODO - Impresion de notas de debito

ACLARACION: El modulo dentro tiene un demonio que es el encargado de
conectarse por medio de XMLRPC y enviar las instrucciones a la impresora.
""",

'depends' : [
    'base',
    'account',
    'l10n_ar_point_of_sale',
    'l10n_ar_account_check',
],

'data': [
	"views/pfiscal_view.xml",
	"views/fis_invoice_view.xml",
	"views/fis_queue_view.xml",
	"views/ar_pos_view.xml",
],

'installable': True,
'application': False,
'auto_install': False,
'active': True

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
