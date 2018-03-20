# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "BnD",
			"color": "#019941",
			"icon": "fa fa-subway",
			"type": "module",
			"label": _("BND")
		},
		{
			"module_name": "Human Resource",
			"color": "#0061A8",
			"icon": "fa fa-users",
			"type": "link",
			"link": "List/Human Resource"
		},
		{
			"module_name": "Shift Schedule Exception",
			"_doctype": "Shift Schedule Exception",
			"color": "#0085A8",
			"icon": "fa fa-calendar-o",
			"type": "link",
			"link": "List/Shift Schedule Exception"
		},
		{
			"module_name": "Upload Shift Schedule",
			"_doctype": "Upload Shift Schedule",
			"color": "#0091A8",
			"icon": "fa fa-upload",
			"type": "link",
			"link": "List/Upload Shift Schedule"
		},
		{
			"module_name": "Attendance",
			"_doctype": "Attendance",
			"color": "#0061A8",
			"icon": "fa fa-check-square",
			"type": "link",
			"link": "List/Attendance"
		},
		{
			"module_name": "Attendance Violation",
			"_doctype": "Attendance Violation",
			"color": "#0061A8",
			"icon": "fa fa-minus-square",
			"type": "link",
			"link": "List/Attendance Violation"
		},
		{
			"module_name": "Device",
			"_doctype": "Device",
			"color": "#cb3fcd",
			"icon": "fa fa-server",
			"type": "link",
			"link": "List/Device"
		},
		{
			"module_name": "Shift Time",
			"_doctype": "Shift Time",
			"color": "#0351A8",
			"icon": "fa fa-calendar-plus-o",
			"type": "link",
			"link": "List/Shift Time"
		},
		{
			"module_name": "Shift Schedule",
			"_doctype": "Shift Schedule",
			"color": "#0061A8",
			"icon": "fa fa-calendar",
			"type": "link",
			"link": "List/Shift Schedule"
		},
		{
			"module_name": "Store",
			"_doctype": "Store",
			"color": "#0061A8",
			"icon": "fa fa-building",
			"type": "link",
			"link": "List/Store"
		}
	]
