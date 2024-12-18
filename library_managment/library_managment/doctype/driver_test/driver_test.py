# Copyright (c) 2024, Abc and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Drivertest(Document):
	def before_save(self):
		if self.last_name:
			self.full_name = self.first_name + " " + self.last_name
		else:
			self.full_name = self.first_name

	
