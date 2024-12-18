
frappe.ui.form.on('Exam', {
	refresh: function(frm) {
		// Disable right-click
document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
    frappe.msgprint({
        title: __('Warning'),
        indicator: 'red',
        message: __('Right-click has been disabled during the exam.')
    });
});

document.addEventListener('keydown', function (e) {
    if (e.key === "F12" || e.key==="Escape" ||(e.ctrlKey && e.shiftKey && e.key === "I") || (e.ctrlKey && e.shiftKey && e.key === "J")) {
        e.preventDefault();
        frappe.msgprint({
            title: __('Warning'),
            indicator: 'red',
            message: __('Developer tools are disabled during the exam.')
        });
    }
});

// Request Full-Screen Mode
if(frm.doc.docstatus==0){
if (document.documentElement.requestFullscreen) {
	document.documentElement.requestFullscreen();
  } else if (document.documentElement.webkitRequestFullscreen) { // Safari/Chrome
	document.documentElement.webkitRequestFullscreen();
  } else if (document.documentElement.msRequestFullscreen) { // IE/Edge
	document.documentElement.msRequestFullscreen();
  }
}
  function disableEscapeKey(e) {
	// Check if the page is in full-screen mode
	if (document.fullscreenElement || document.webkitFullscreenElement || document.msFullscreenElement) {
		if (e.key === "Escape") {
			e.preventDefault(); // Disable Escape key
		}
	}
}

// Attach the event listener to disable Escape key in full-screen mode
document.addEventListener('keydown', disableEscapeKey);
 
		// let tabSwitchCount = 0;

		// window.addEventListener("blur", () => {
		// 	tabSwitchCount++;
		// 	frappe.msgprint({
		// 		title: __('Warning'),
		// 		indicator: 'red',
		// 		message: __('You switched tabs.You have been disqualified for switching tabs.')
		// 	});
		// });
		
		// window.addEventListener("focus", () => {
		// 	console.log("User returned to the tab");
		// 	autoSubmitExam(frm);
		// });
		
         
		// function autoSubmitExam(frm) {

		// 	frappe.call({
		// 		method : "frappe.client.submit",
		// 		args : {
		// 			doc:frm.doc
		// 		},
		// 		callback:function(r){
		// 			if(!r.exc){
        //            frappe.msgprint("your exam has been submitted").then(() => {
		// 			$('.standard-actions .btn-primary').hide();
		// 			// Hide the Save button after showing the message
		// 			// frm.disable_save();
		// 			frm.set_df_property("", "read_only", frm.is_new() ? 0 : 1);
		// 		});
				
		// 		$(document).ready(function() {
		// 			// $('.btn btn-primary btn-sm primary-action').hide(); 
		// 			$('.standard-actions .btn-primary').hide();
		// 		})
		// 		// $('.btn.btn-primary.btn-sm.primary-action').prop('disabled', true)
		
		// 		}
			
		// 		}}
		// 	)
	
		// 	console.log("disqualify")
		// 	console.log(frm.doc)
			
		// };

	},

validate: function (frm) {
	// Exit Full-Screen Mode after Submit
	if (document.exitFullscreen) {
	  document.exitFullscreen();
	} else if (document.webkitExitFullscreen) {
	  document.webkitExitFullscreen();
	} else if (document.msExitFullscreen) {
	  document.msExitFullscreen();
	}
  },
  
}
);

