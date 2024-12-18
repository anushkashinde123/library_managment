// Copyright (c) 2024, Abc and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Member', {
	
		refresh: function(frm) {

			// frm.set_df_property('get_otp', 'reqd', 1);
			if(frm.doc.__islocal==1){
				console.log('true')
				// frm.set_df_property('get_otp','hidden','1')
			
			} else{
				console.log('false')
				// frm.set_df_property('get_otp','hidden','0')
			}
			
			
			frm.add_custom_button("Creat Membership",()=>{
				frappe.new_doc("Library Membership",{
					library_member:frm.doc.name
				})
			})
			frm.add_custom_button("Create transaction",()=>{
				frappe.new_doc("Library Transaction",{
					library_member:frm.doc.name
				})
			})
			
			// frm.add_custom_button('Return',()=>
			// frappe.msgprint("Returned"))
		   

			var today = new Date(); 
			var birthDate = new Date(frm.doc.date_of_birth); 
			var age = today.getFullYear() - birthDate.getFullYear(); 
			var m = today.getMonth() - birthDate.getMonth(); 
			if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) 
				{ 
			      age--; 
				  } 
				//   frm.set_value('age', age);
				//   return age;

				}
			


        //  frappe.msgprint({
		// 	title : __('Notification'),
		// 	indicator:'green',
			// message:"Congratulations..Member has been added successfully.",
			// primary_action:{
			// 	'label' :'Proceed',
			// 	'server_action':'dotted.path.to_method',
			// 	'client_action':'dotted.path.to_method',
			// 	'args':args}
			// })

			// let d = new frappe.ui.Dialog({
			// 	title : "Enter Details",
			// 	fields:[
			// 		{
			// 			label : 'First_name',
			// 			fieldname : 'first_name',
			// 			fieldtype : 'Data'

			// 		},
			// 		{
			// 			label : 'Last_name',
			// 			fieldname : 'last_name',
			// 			fieldtype : 'Data'
			// 		}
			// 	],
			// 	size :'small',
			// 	primary_action_label :'Submit'

					
				
			// })
			// d.show()

			// frappe.prompt("First Name",({ value })=> console.log(value))

		,get_otp:function(frm){
			console.log('clicked get otp')
			frappe.call({
				args : {
					doc : frm.doc,
					email : frm.doc.email
		
				},
				method: 'library_managment.library_managment.doctype.library_member.library_member.getotp',
				callback:function(r){
                console.log([r.message])
		        frappe.msgprint("Otp is successfully sent to your mail")
				let d = new frappe.ui.Dialog({title:'Otp verification',
						fields:
                                [
									{
										label:'Enter your otp',
										fieldname:'enter_otp',
										fieldtype:'Data'
									}			
								],
						primary_action_label:"Submit",
						primary_action(values){
				        // $('.modal-backdrop').unbind('click');
			            //  console.log(values.enter_otp)
							console.log(r.message)
							if(values.enter_otp==r.message){
								frappe.msgprint("OTP verified successfully")
							}else{
								frappe.throw("Invalid Otp.")
							}
			  
							d.hide();					
							},
						static : true
               });
				d.show();
				}
			})
		},
		// validate:function(frm){
		// 	lm = frappe.get_doc('Library Member','library_member')
		// 	if(frm.doc.enter_otp==lm.get_otp){
		// 		frappe.msgprint("success")
		// 	}else
		// 	{
		// 	  frappe.msgprint("not valid")
		// 	}
		// }
		// enter_otp:function(frm){
		// 	console.log('clicked enter otp')
		// 	console.log(frm.doc.enter_otp)
		// 	frappe.call({
		// 		method:'library_managment.library_managment.doctype.library_member.library_member.getotp',
		// 		args : {
		// 			doc : frm.doc,
		// 			email : frm.doc.email,
		// 			enter_otp : frm.doc.enter_otp

		// 		},
		// 		callback:function(r){
		// 			console.log(r.message)
		// 			console.log(frm.doc.enter_otp)
		// 			if(r.message==frm.doc.enter_otp){
        //                 frappe.msgprint("success")
		// 			}else{
		// 				frappe.msgprint("not valid")
		// 			}

		// 		}
			// })
		// }
		});
		frappe.ui.form.on('LM Child',{
			button:function(frm,cdt,cdn){
				var row = locals[cdt][cdn]
				console.log(row)
				if(row.type==="Issued"){
                // frm.set_value('type','Return').then(()=>{frappe.msgprint('changed')})
				// frm.save()
				frappe.call(
					{
						method :'frappe.client.insert',
						args : {
							doc:{
								doctype:'Library Transaction',
								type:'Return',
								date_of_transaction:frappe.datetime.now_date(),
								library_member:frm.doc.name,
							    article : row.article,
								docstatus:1

							}
						},
						
						callback:function(r){
							frappe.msgprint('Selected book is book returned')
						}
					}
				)}else{
					frappe.msgprint("Book is alredy returned")
				}
				//  frappe.msgprint("Returned")

				
			}})
