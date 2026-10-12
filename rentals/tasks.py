import frappe
def send_daily_rental_reminders():
    """Find all active bookings and log daily status check."""
    active_bookings = frappe.get_all("Ride Booking", filters={"docstatus": 1})
    frappe.logger().info(f"Daily Check: {len(active_bookings)} active ride bookings found.")