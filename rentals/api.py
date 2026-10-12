import frappe

@frappe.whitelist(allow_guest=True)
def get_available_drivers():
    """Returns list of enabled drivers with their license details."""
    drivers = frappe.get_all(
        "Driver",
        fields=["name", "first_name", "last_name", "phone_number", "license_number"],
        filters={"enabled": 1}
    )
    return drivers

@frappe.whitelist()
def todo_before_insert(doc, method):
    # Automatically append a prefix to all new ToDo descriptions
    doc.description = f"[Rentals App Notice] {doc.description}"