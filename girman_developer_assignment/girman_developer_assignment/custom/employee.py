import frappe
from frappe.utils.pdf import get_pdf

def generate_experience_certificate(doc, method):
    if doc.workflow_state == "Exit":
        try:
            # Render HTML using print format
            html = frappe.get_print("Employee", doc.name, print_format="Experience Certificate")

            # Convert HTML to PDF
            pdf_content = get_pdf(html)

            # Attach PDF to Employee doc
            file = frappe.get_doc({
                "doctype": "File",
                "file_name": f"Experience_certificate_{doc.employee_name}.pdf",
                "attached_to_doctype": "Employee",
                "attached_to_name": doc.name,
                "content": pdf_content,
                "is_private": 1
            })
            file.insert(ignore_permissions=True)

            frappe.msgprint(f"Experience Certificate generated for {doc.employee_name}")

        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Experience Certificate Generation Failed")
            frappe.msgprint(f"Error while generating Experience Certificate: {e}")


def set_automation_status(doc,method):
    #Set Status Active
    if doc.workflow_state == "Confirmation":
        doc.status = "Active"
    
    #Set Status Inactive
    elif doc.workflow_state == "Joining":
        doc.status = "Inactive"

    #Set Status Left
    elif doc.workflow_state == "Exit":
        doc.status = "Left"

