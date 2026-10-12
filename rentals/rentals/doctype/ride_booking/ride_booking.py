# Copyright (c) 2026, dev and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		if not self.rate:
			# Fetch standard rate from Single DocType if rate is not set
			self.rate = frappe.db.get_single_value("Rentals Settings", "standard_rate") or 10

		# Calculate total distance across all child table rows
		total_distance = sum(trip_details.distance or 0 for trip_details in self.trip_details)

		# Calculate total amount
		self.total_amount = total_distance * (self.rate or 0)
