frappe.ui.form.on('Lead',{
    refresh:function(frm)
    {
        console.log("hi 123")
        frm.add_custom_button(__("Qualify Lead"),function(){

            frappe.call(
                {   args:{
                        doc : frm.doc,
                        name : frm.doc.name
                
                     },
                    method :"library_managment.library_managment.custom_script.lead.lead.custom_button",
                    callback : function(r){
                        frappe.msgprint(r.message)
                    }
                }
            )

            
            // frappe.msgprint("Custom Button Clicked by user");
        });
    }

 })