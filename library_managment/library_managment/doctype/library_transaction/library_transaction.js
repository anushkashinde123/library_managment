// Copyright (c) 2024, Abc and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
	refresh(frm) {
		frm.set_query('article',()=>{
			return{
			filters:{
				status:'Available'
			}}});

		membership = frappe.db.get_value('Library Membership','name','workflow_state')
		frm.set_query('library_member',()=>{
			return{
				filters:{
					membership:1
				}
                  
				
			}
		})


}
});


