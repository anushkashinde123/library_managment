// Copyright (c) 2024, Abc and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {
	refresh: function(frm) {
       frm.add_custom_button("Payment",()=>{
		frappe.new_doc('Payment',{
			library_member : frm.doc.library_member
		})
	   })
	}

});
