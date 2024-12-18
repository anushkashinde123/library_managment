# Copyright (c) 2024, Abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus 
from frappe.utils import add_to_date,date_diff

class LibraryMembership(Document):
	def before_save(self):
		date_1 = self.from_date
		date_2 = add_to_date(date_1,years=1)
		self.to_date = date_2
		print("======",self.paid)
		if frappe.db.exists('Payment',{'library_member':self.library_member}):
			self.paid = 1
		

	def before_submit(self):
		exists = frappe.db.exists(
			"Library Membership",
		{
				'docstatus':DocStatus.submitted(),
				'to_date':('>',self.from_date),
				'library_member':self.library_member

		},
	)
		if exists:
			frappe.throw("There is active membership for this member")

		if self.paid!=1:
			frappe.throw("Please pay by doing payment for taking memebership")


		# loan_period = frappe.db.get_single_value('Library Settings','loan_period')
		# self.to_date = frappe.utils.add_days(self.from_date,loan_period or 30)
	
	# def validate(self):
	# 	t = today()
	# 	valid_till = frappe.db.get_value('Library Membership',self.library_member,self.to_date)
	# 	diff = date_diff() 

	# refresh: function(frm) {
	# 	var today = new Date(); 
	# 	var birthDate = new Date(frm.doc.to_date); 
	# 	var age = today.getFullYear() - birthDate.getFullYear(); 
	# 	var m = today.getMonth() - birthDate.getMonth(); 
	# 	if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) 
	# 		{ 
	# 		  age--; 
	# 		  } 
	# 		  frm.set_value('age', today.getFullYear());
	# 		//   return age;
    #      }






		

	
