frappe.pages['library-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Library page',
		single_column: true
	});

    page.set_title('My Library Page')
	page.set_indicator('Done','green')

	let btn = page.set_primary_action('New',()=> frappe.msgprint('Clicked new'));

	page.add_menu_item('Send Email',()=> frappe.msgprint('Clicked send email'))

	page.add_action_item("Delete",()=> frappe.msgprint("clicked delete button"))

	let field = page.add_field({
		label:'Status',
		fieldname : 'status',
		fieldtype : 'Select',
		options :[ 'Open',
		          'closed',
				  'cancelled'],

        change(){
			frappe.msgprint(field.get_value());
		}

	});

	// Rendering html
	// $(frappe.render_template('library_page',{})).appendTo(page.body)

	$(frappe.render_template('library_page',{
        data : 'Welcome to Library Page'
	})).appendTo(page.body)

}