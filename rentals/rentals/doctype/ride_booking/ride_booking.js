// Copyright (c) 2026, dev and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {
		// Add a custom action button if the booking is submitted
		if (frm.doc.docstatus === 1) {
			frm.add_custom_button(
				__("Print Summary"),
				function () {
					frappe.show_alert({
						message: __("Preparing summary for ") + frm.doc.name,
						indicator: "blue",
					});
				},
				__("Actions"),
			);
		}
	},
	rate(frm) {
		// Recalculate total when rate changes
		calculate_total(frm);
	},
});

// Listen to child table distance changes
frappe.ui.form.on("Ride Booking Item", {
	distance(frm, cdt, cdn) {
		calculate_total(frm);
	},
	trip_details_add(frm) {
		calculate_total(frm);
	},
	trip_details_remove(frm) {
		calculate_total(frm);
	},
});

function calculate_total(frm) {
	let total_distance = 0;
	(frm.doc.trip_details || []).forEach((row) => {
		total_distance += row.distance || 0;
	});
	let total_amount = total_distance * (frm.doc.rate || 0);
	frm.set_value("total_amount", total_amount);
}
