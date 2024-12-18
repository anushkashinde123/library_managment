// Copyright (c) 2024, Abc and contributors
// For license information, please see license.txt



frappe.ui.form.on('Article',{ 
	refresh: function(frm) {
 
// setup(frm)
// {
//    frappe.msgprint("frm is set up");
// }


// frm.set_value('author','author_name')
// frm.refresh();
// frm.refresh_field("description");
// frm.set_query('article',function(){
// 	return{
// 	filters:{'status':'Available'}
// 	};
// });

if(frm.is_dirty){
   frappe.show_alert("Please save your changes before attaching a file")
}

		if(!frm.is_new()){
			frm.add_custom_button("Click Custom button",()=>console.log("Clicked custom button"))
		}
    

		if(!frm.doc.decription){
			console.log("Clicked custom button")
			frm.set_intro("please add some value to the description","blue");
		}

		frm.add_custom_button("Open reference form",()=>{frappe.set_route('Form', frm.doc.reference_type, frm.doc.reference_name);})
	    
        frm.add_custom_button("Closed",()=>{
			frm.doc.status='Closed'
		},"Set Status")

		frm.change_custom_button_type("Click Custom button",null,'primary')
		frm.change_custom_button_type("Closed",'Set Status','danger')

		// frm.remove_custom_button("Click Custom button")
		// frm.clear_custom_buttons();

		frm.set_df_property("description",'feildtype','Text')
		// frm.set_df_property("status","options",['Open','Closed'])
		frm.set_df_property("author","reqd",1)
		frm.set_df_property("status","read-only",1)

		let is_allowed = frappe.user_role.includes("System Manager")
		frm.toggle_enable('publisher',is_allowed)

		// frm.toggle_reqd('priority',frm.doc.status==='Open')
		// frm.toggle_display(['priority'],frm.doc.status==='Open')

		frm.set_query("publisher",()=> {return
			{
              filters:{
				
			  }
            }})

		
		frm.trigger('set_mandatory_fields')

		
	
		// set_mandatory_fields('priority',frm.doc.status==='Open')
	}
});
