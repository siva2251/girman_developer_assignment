import frappe

def update_investment_deductions(doc, method):
    investments = frappe.db.get_value(
        "Employee Investment Declaration",
        {"employee": doc.employee},
        ["section_80c", "section_80d", "other_exemptions"],
        as_dict=True
    ) or {}

    if investments:
        mapping = {
            "section_80c": "Section 80C",
            "section_80d": "Section 80D",
            "other_exemptions": "Other Exemptions"
        }

        for key, component in mapping.items():
            amount = investments.get(key) or 0
            if amount:
                found = False
                for d in doc.deductions:
                    if d.salary_component == component:
                        d.amount = amount
                        found = True
                        break
                if not found:
                    doc.append("deductions", {
                        "salary_component": component,
                        "amount": amount
                    })

    # 🔹 Recalculate totals so deductions are included
    doc.calculate_net_pay()
    doc.compute_year_to_date()
