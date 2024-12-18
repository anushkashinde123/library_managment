// Copyright (c) 2024, Abc and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Library Transaction Script Report"] = {
	"filters": [
		{
			'fieldname':'library_member',
			'fieldtype':'Link',
			'label':__('Member'),
			'options':"Library Member"
		},
		
		{
			'fieldname':'from_date' ,
			'fieldtype': 'Date',
			'label':__('From Date'),
		},
		{
			'fieldname':'to_date' ,
			'fieldtype': 'Date',
			'label':__('To Date'),
		},
	
		{
			'fieldname':'article',
			'fieldtype':'Link',
			'label':__("Article"),
			'options':"Article"
		},
		// {
		// 	'fieldname':'type' ,
		// 	'fieldtype': 'Select',
		// 	'label':__('Type'),
		// 	'options':["Issued","Return"]
		// }

	],

	"formatter":function (row, value, columns, data, default_formatter) {
	value = default_formatter(row,value, columns, data);
	if (columns.fieldname == "type" && value == 'Issued') {
		value = "<span style='color:red;'>" + value + "</span>";
	}
	if(columns.fieldname == 'type'&& value=='Return'){
		value= "<span style='color:green'>"+ value +"</span>";
	}
	return value;
}

};
