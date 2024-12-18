import frappe
from frappe.model.document import Document

def test(doc,method=None):
    # frappe.msgprint("Saved successfully")
    print("__success")

@frappe.whitelist()
def custom_button(name):
    doc = frappe.get_doc('Lead',name)
    # doc = frappe.db.get_value('Lead','CRM-LEAD-2024-00007','qualification_status')
    print("-----",doc.qualification_status)
    if doc.qualification_status!='Qualified':
        doc.qualification_status='Qualified'
        doc.save(ignore_permissions=True)
        frappe.msgprint("Lead is qualified")
    else:
        frappe.msgprint("Lead is already qualified")
    # return "Lead is qualified"