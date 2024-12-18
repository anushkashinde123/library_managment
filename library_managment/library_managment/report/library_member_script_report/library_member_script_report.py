# Copyright (c) 2024, Abc and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	if not filters:
		filters = {}

	columns, data = [], []

	columns = get_columns(data)
	cs_data = get_cs_data(filters)

	if not cs_data:
		frappe.msgprint("No record found")
		return columns,data
	
	data = []
	for d in cs_data:
		row = frappe._dict({
			'name':d.name,
			'age':d.age
			# 'lm_child':d.lm_child

		})
		data.append(row)

	
	return columns, data,None

def get_columns(self):
	return [
		{
			'fieldname':'name',
			'fieldtype':'Link',
			'label':_("Library Member"),
			'options':'Library Member'
		},
		# {
		# 	'fieldname':'name',
		# 	'fieldtype':'Table',
		# 	'label':_("Library child"),
		# 	'options':'LM Child'

		# },
		{
			'fieldname':'age',
			'fieldtype':'Data',
			'label':_("Age")
		}
	]


def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype = 'Library Member',
		fields = ['name','age'],
		filters = conditions
	)
	return data


def get_conditions(filters):
	conditions = {}
	for key,value in filters.items():
		if filters.get(key):
			conditions[key] = value
	return conditions

