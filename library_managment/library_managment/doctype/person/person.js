// Copyright (c) 2024, Abc and contributors
// For license information, please see license.txt

frappe.ui.form.on('Person', {
	refresh: function(frm) {
	
	// frm.set_query('first_name',()=>{
    //      return{
	// 		filters:
	// 	 }
	// }

	// })

     if(frm.is_dirty){
		frappe.show_alert("please save before attachment");
	 }

	 if(!frm.doc.description){

		frm.set_intro("Please add description",'blue');
	 }
      if(frm.is_new){
	 frm.add_custom_button("custom",()=>(console.log("clicked")))
	  }
	//  if
	frm.change_custom_button_type("custom",null,'primary')

	frm.set_df_property("status",'reqd',1)

	frm.toggle_reqd('priority',frm.doc.status==='open')

	// Document Api

	// doc = frappe.get_doc('singular')
	// doc.timezone

	doc = frappe.get_doc({
		'doctype':'person',
		'title' : 'new person'
	})
	doc.insert()

	}
});
