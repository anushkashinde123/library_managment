# Copyright (c) 2024, Abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Payment(Document):
	def before_save(self):
		fee = frappe.db.get_single_value('Library Settings','fee')
		self.fee = fee

@frappe.whitelist()
def fee(lm,paid_amount):
	doc1 = frappe.db.get_value('Library Membership',{'library_member': lm},'paid')
	if doc1 == 1:
		frappe.msgprint("Already Paid")
	else:
		doc1 = 1

	# doc = frappe.new_doc('Payment Entry')
	# doc.payment_type = 'Pay'
	# doc.party_type = 'Employee'
    # doc.party = lm
	# # print("======",paid_amount)
	# doc.paid_amount = paid_amount
	# doc.received_amount = paid_amount
	# doc.source_exchange_rate = 1
	# doc.save()
	
	

	
	
