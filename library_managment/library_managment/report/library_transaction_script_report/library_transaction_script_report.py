# Copyright (c) 2024, Abc and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):

	if not filters:
		filters = {}
	columns, data = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data: 
		frappe.msgprint(_("No records found"))
		return columns, cs_data

	data = []
	for d in cs_data:
		row = frappe._dict({
			'library_member':d.library_member,
			'date_of_transaction':d.date_of_transaction,
			'article':d.article,
			'type':d.type
		})
		data.append(row)

	chart = get_chart_data(data)
	report_summary = get_report_summary(data)

	return columns,data,None,chart,report_summary


def get_columns():

	return [
		{
			'fieldname':'library_member' ,
			'fieldtype':'Link',
			'label':_("Library Member"),
			'options':"Library Member",
			'width':'150'
			
		},
		{
			'fieldname':'date_of_transaction' ,
			'fieldtype':'Date',
			'label':_('Date of transaction'),
			'width':'150'
		}
		,
		{
			'fieldname':'article',
			'fieldtype':'Data',
			'label':_("Article"),
			'width':'150'
		},
		{
			'fieldname':'type',
			'fieldtype':'Data',
			'label':_("Type"),
			'width':'150'

		}	
	]
from frappe.utils import getdate
def get_cs_data(filters):

	# conditions = get_conditions(filters)
	# conditions=[]

	# # # print("\n\n filters.get(from_date) and filters.get(to_date):", filters.get("from_date"), filters.get("to_date"))

	# if filters.get("from_date") and filters.get("to_date"):
	# 	conditions.append(['date_of_transaction','>=', getdate(filters.get("from_date"))])
	# 	conditions.append(['date_of_transaction','<=',getdate(filters.get("to_date"))])

	# if filters.get('library_member'):
	# 	conditions.append({"library_member" : filters.get('library_member')})

	# if filters.get('article'):
	# 	conditions.append({'article' : filters.get('article')})

	# data = frappe.get_all(
	# 		doctype = "Library Transaction",
	# 		fields = ['library_member','date_of_transaction','article','type'],
	# 		filters = conditions
	# )

	# conditions=""
	# if filters.get("from_date") and filters.get("to_date"):
	# 	conditions+= f""" and date_of_transaction between '{filters.get('from_date')}'
	# 				and '{filters.get('to_date')}' """

	# if filters.get('library_member'):
	# 	conditions += f" and library_member = '{filters.get('library_member')}'"
    
	# if filters.get('article'):
	# 	conditions += f" and article = '{filters.get('article')}'"

	# data = frappe.db.sql(f"""select *
	# from `tabLibrary Transaction` where 1=1 {conditions}
	# """,as_dict=1, debug=1)
	# print(data)

	conditions="where 1=1"
	if filters.get("from_date") and filters.get("to_date"):
		value = {'from_date':filters.get('from_date'),'to_date':filters.get('to_date')}
		conditions += " and date_of_transaction between '%(from_date)s' and '%(to_date)s'"% value

	if filters.get('article'):
		conditions += " and article = '%(article)s'" % {'article' : filters.get('article')}

	if filters.get('library_member'):
		conditions += " and library_member = '%(library_member)s'"%{'library_member':filters.get('library_member')}

	# data = frappe.db.sql("""select *
	# from `tabLibrary Transaction` where 1=1 {0} """.format(
	# 	conditions
	# ), as_dict=1)
	
	data = frappe.db.sql("""select *
	from `tabLibrary Transaction` %(condition)s;"""%
	 {'condition':conditions},as_dict=1
	)
	return data

# def get_conditions(filters):
# 	conditions = {}
# 	for key,value in filters.items():
# 		if filters.get(key):
# 			conditions[key]=value
# 	return conditions

def get_chart_data(data):
	if not data:
		return None

	labels = ['Issued','Return']
	type_data = {
		'Issued':0,
		'Return':0,
	}
	datasets = []

	for entry in data:
		if entry.type=='Return':
			type_data['Return']+=1

		else:
			type_data['Issued']+=1

	datasets.append({
		'name':'Type',
		'values':[type_data.get('Issued'),type_data.get('Return')]
	})

	chart = {
		'data':{
			'labels':labels,
			'datasets':datasets
		},
		'type':'pie',
		'height':100,
		'width':10

	}
	return chart

def get_report_summary(data):
	if not data:
		return None
	type_issued , type_return = 0,0

	for entry in data:
		if (entry.type=="Issued" or entry.type=="Issue"):
			type_issued += 1
		else:
			type_return += 1
	return [
		{
			'value':type_issued,
			"indicator":'Green',
			 'label':"Issued Articles",
			# 'datatype':'Int',
		},
		{
			'value':type_return,
			"indicator":'Blue',
			'label':'Returned Articles',
			# 'datatype':'Int'
		},
	]

			
