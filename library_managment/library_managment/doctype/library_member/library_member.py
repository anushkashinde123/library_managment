# Copyright (c) 2024, Abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today,date_diff
import random,math


class LibraryMember(Document):
	# def after_save(self):
	# 	frappe.msgprint("Member has been added successfully")
	
	def before_save(self):
		self.full_name = f"{self.name1} {self.last_name}"


	def validate(self):
		if self.user_created==0:
			doc = frappe.new_doc('User')
			doc.first_name = self.name1
			doc.email = self.email
			doc.append('roles',{'Doctype':'Has Role',"role":'Library Member'})
			doc.insert(ignore_permissions=True)
			doc.save()
			if frappe.db.exists('User',self.email):
				self.user_created = 1
		

		doc = frappe.new_doc('User Permission')
		doc.update({
			'user':self.email,
			'allow':'Library Member',
			'for_value': self.name
		})
		doc.insert(ignore_permissions=True)
		doc.submit()
		 
	# 	if self.enter_otp == getotp():
	# 		print("====true")
	# 	if self.age <= 18:
	# 		frappe.throw("Age must be greater than 18")

	# def validate(self):
	# 	# t = today()
	# 	# print(today)
	# 	# valid_till = frappe.get_doc('Library Membership',self.library_member)
	# 	# # valid_till = frappe.db.get_value('Library Membership',self.library_member,'to_date')
	# 	# print(valid_till.to_date)
	# 	# diff = date_diff(valid_till,t)
	# 	self.validity = 9
	# 	print(self.validity)

	# def before_save(self):
	# 	doc_otp = frappe.get_all('Otp',filters={'email':self.email},fields=['otp'],
	# 	order_by='creation desc',limit=1)
	# 	print("=====",doc_otp[0].get('otp'))
	# 	print(self.enter_otp)
	# 	if doc_otp and doc_otp[0].get('otp')==self.enter_otp:
	# 		frappe.msgprint("valid")
	# 	else:
	# 		frappe.msgprint('Invalid')

	
			


@frappe.whitelist()
def getotp(email):
	digits = "0123456789"
	otp = ""
	for i in range(4):
		otp += digits[math.floor(random.random() * 10)]
	# return otp
	mail = frappe.sendmail([email],subject='Otp For library member',
							message = f"Your otp is:{otp}",
	                        as_markdown = True
	)
	# lm = frappe.new_doc('Otp')
	# lm.otp = otp
	# lm.email = email
	# lm.save()

	

	return otp
	# if mail:
	# 	if enter_otp != otp :
	# 		frappe.throw("Invalid otp")

	



# print(getotp())

	

			
		
    
 		

	



		

	

