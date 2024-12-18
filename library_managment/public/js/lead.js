frappe.ui.form.on('Lead',{
    refresh:function(frm)
    {
        console.log("hi")
        frm.add_custom_button(__("Add Custom Button"),function(){
            frappe.msgprint("Custom Button Clicked by user");
        });
    }

 })