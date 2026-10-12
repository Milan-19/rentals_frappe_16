# Copyright (c) 2026, dev and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	def before_save(self):
		last = f"{self.last_name}" if self.last_name else ""
		self.full_name = f"{self.first_name} {last}"
