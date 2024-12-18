// Copyright (c) 2024, Abc and contributors
// For license information, please see license.txt

frappe.ui.form.on('Payment', {
	// refresh: function(frm) {

	// }
	pay_fee : function(frm){
		// frappe.msgprint("Paid successfully!!")
		frappe.call({
			args : {
				doc : frm.doc,
				lm : frm.doc.library_member,
				paid_amount : frm.doc.fee
			},
			method : "library_managment.library_managment.doctype.payment.payment.fee",
			callback:function(){
               frappe.msgprint("payment success!!")
			}
		})
		
	}
});
