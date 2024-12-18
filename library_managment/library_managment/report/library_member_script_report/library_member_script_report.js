// Copyright (c) 2024, Abc and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Library Member Script Report"] = {
	"filters": [
		{
			'fieldname':'name',
			'fieldtype':'Link',
			'label':__("Library Member"),
			'options':'Library Member'
		}
		// ,
		// {
        //     'fieldname':'article',
		// 	'fieldtype':'Link',
		// 	'label':'Article',
		// 	'options':'LM Child'

		// }
   
	]
};
