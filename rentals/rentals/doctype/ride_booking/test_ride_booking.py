# Copyright (c) 2026, dev and Contributors
# See license.txt


import frappe
from frappe.tests.utils import FrappeTestCase
class TestRideBooking(FrappeTestCase):
	def test_total_amount_calculation(self):
		# 1\. Create a temporary test driver
		driver = frappe.get_doc({ "doctype": "Driver", "first_name": "Test", "last_name": "Driver", "license_number": "TEST-LIC-123" }).insert()
		# 2\. Create a temporary test vehicle
		vehicle = frappe.get_doc({ "doctype": "Vehicle", "make": "Audi", "model": "R8", "year": 2024 }).insert() # 3\. Instantiate Ride Booking document
		booking = frappe.new_doc("Ride Booking")
		booking.driver = driver.name
		booking.vehicle = vehicle.name
		booking.rate = 10
		# Append child table rows using append()
		booking.append("trip_details", { "source": "Dubai Mall", "destination": "Marina", "distance": 15 })
		booking.append("trip_details", { "source": "Marina", "destination": "Airport", "distance": 25 })
		# Insert triggers validate() controller logic
		booking.insert()
		# Assert total distance (15 + 25 = 40) * rate (10) == 400
		self.assertEqual(booking.total_amount, 400)
# # import frappe
# from frappe.tests import IntegrationTestCase


# # On IntegrationTestCase, the doctype test records and all
# # link-field test record dependencies are recursively loaded
# # Use these module variables to add/remove to/from that list
# EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
# IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



# class IntegrationTestRideBooking(IntegrationTestCase):
# 	"""
# 	Integration tests for RideBooking.
# 	Use this class for testing interactions between multiple components.
# 	"""

# 	pass
