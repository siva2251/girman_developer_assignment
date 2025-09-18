import frappe

def set_salary_structure(doc,method):
    if doc.employee:
        employee = frappe.get_doc("Employee", doc.employee)

        #Set Tax Regime Based On Employee Doc
        if employee.custom_tax_regime_preference == "Old Regime":
            doc.salary_structure = "Old Regime"
        elif employee.custom_tax_regime_preference == "New Regime":
            doc.salary_structure = "New Regime"