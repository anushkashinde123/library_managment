# Copyright (c) 2024, Abc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus
from datetime import datetime
from frappe.utils import add_to_date

class LibraryTransaction(Document):

		
	def before_submit(self):
		article = frappe.get_doc('Article',self.article)
		if self.type == 'Issued':
			self.validate_issue()
			self.validate_maximum_limit()
			article = frappe.get_doc('Article',self.article)
			article.status = 'Issued'
			article.save()
	
		elif self.type == 'Return':
			self.validate_return()
			# self.validate_delay()
			article = frappe.get_doc('Article',self.article)
			article.status = 'Available'
			article.save()
			
	
	def validate_issue(self):
		self.validate_membership()
		article = frappe.get_doc("Article",self.article)
		
		# if article.status=='Issued':
		# 	frappe.throw("Artical is already issued by another member")
	
		if article.status=='Issued':
			article.book_qty-=1
			article.save(ignore_permissions=True)
			if article.book_qty==0:
				frappe.throw('book is not available')
		elif article.status=='Return':
			article.book_qty+=1
			article.save(ignore_permissions=True)


	def validate_return(self):
		self.validate_membership()
		article = frappe.get_doc("Article",self.article)
		if article.status == "Available":
			frappe.throw("Artical can't be returned without being issued")
			

	def validate_maximum_limit(self):
		max_articles = frappe.db.get_single_value('Library Settings','max_articles')
		count = frappe.db.count(
			"Library Transaction",{
				'library_member': self.library_member,
				'type':'Issued',
				'docstatus': DocStatus.submitted()
			})
		count2 = frappe.db.count(
			"Library Transaction",{
				'library_member': self.library_member,
				'type':'Return',
				'docstatus': DocStatus.submitted()
			}
		)
		count3 = count-count2
		if count3 >= max_articles:
			frappe.throw("Maximum limits reached for issueing documents")

	def validate_membership(self):
		valid_membership = frappe.db.exists(
			"Library Membership",
			{
				'library_member':self.library_member,
				'docstatus':DocStatus.submitted(),
				'from_date':('<',self.date_of_transaction),
				'to_date'  :('>',self.date_of_transaction)

			},
		)
		if not valid_membership:
			frappe.throw('No valid membership')

	def on_submit(self):
		l_member = frappe.get_doc('Library Member',self.library_member) 
		print('\n\nadded',l_member)
		if l_member:
			l_member.append("lm_child",
			{
				"article":self.article,
				"transaction_id":self.name,
				'type':self.type,
				'date':self.date_of_transaction,
			
			})
			# l_member.age=23
			l_member.save(ignore_permissions=True)

		# d = frappe.db.get_value("Library Transaction",
		# {
		# 	'type':'Issued',
		# 	'article':self.article,
		# 	'library_member':self.library_member
		# },
		# self.date_of_transaction)
		# print(d)
		# if self.type=='Return':
		# 	if d < self.date_of_transaction:
		# 		frappe.throw("Delay")
		
	
	def on_cancel(self):
		#  l_member = frappe.get_doc('Library Member',self.library_member)
		q = frappe.db.sql(f"select name from `tabLM Child` where transaction_id='{self.name}'", as_dict=1)
		l = frappe.get_doc('LM Child',q[0].name)
		l.delete()
		#  q.save(ignore_permissions=True)
		
	def validate(self):
		l_settings = frappe.db.get_single_value('Library Settings','loan_period')
		if self.type=='Issued':
			transaction_date = self.date_of_transaction
			self.date_of_return = add_to_date(transaction_date,days=l_settings,as_string=True)
		elif self.type=='Return':
			self.date_of_return = self.date_of_transaction
		

	# def on_save(self):
	# 	today = getdate()
	# 	valid_till = frappe.db.get_value('Library Membership','library_member','to_date')
	# 	diff = date_diff(valid_till,today)
	# 	self.validity = diff
	# 	doc.save(ignore_permissions=True)


	# def validate_delay(self):
	# 	d = frappe.get_value("Library Transaction",
	# 	{
	# 		'type':'Issued',
	# 		'article':self.article,
	# 		'library_member':self.library_member
	# 	},
	# 	self.date_of_return)
		
	# 	if d < self.date_of_transaction:
	# 			self.delay += 1
	# 			print("=========",self.delay)
			

			
