# Copyright (c) 2024, Abc and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDrivertest(FrappeTestCase):
	def test_fullname(self):
		test_driver = frappe.get_doc({
			'doctype':'Driver test',
			'first_name':'Anu',
			'last_name':'Shinde'
		}).insert()
		self.assertEqual(test_driver.full_name,"Anu Shinde")
