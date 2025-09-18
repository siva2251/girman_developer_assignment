### Girman Developer Assignment - Frappe/ERPNext

Application for Assessment

### Setup Instructions

1. **Clone Repository**

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/siva2251/girman_developer_assignment.git --branch develop
bench --site your-site-name install-app girman_developer_assignment
```
2. **Migrate & Build**

```bash
bench --site your-site-name migrate
bench build
bench clear-cache
```

3. **Login Credentials**

Role Based Users created:

* HR Manager
* Interviewer
* Hiring Manager


Default Admin:

```bash
username: Administrator
password: admin
```
### ✅ Features Implemented

**Part 1 – HRMS & Recruitment**
Custom Recruitment Workflow:

* Application → Screening → Interview → Offer → Hired
* Role-based permissions (HR Manager, Interviewer, Hiring Manager).
* Added custom field Source of Application in Job Applicant.
* Recruitment Dashboard and Report: 
   * Chart showing applicants count grouped by Source of Application.

**Part 2 – Employee Lifecycle**

* Workflow: Joining → Probation → Confirmation → Exit.
* Automation:
  * On Confirmation → status auto-updates.
  * On Exit → system generates an Experience Letter PDF attached to Employee record.

**Part 3 – Salary Structure & Payroll**

* Salary Structure with Basic, HRA, Special Allowance, PF, Professional Tax.
* Payroll Entry for multiple employees.
* Custom Payroll Slip print format with branding.

**Part 4 – Tax Regime Implementation**

* Two Salary Structures: Old Regime & New Regime.
* Custom field in Employee: Tax Regime Preference.
* Payroll picks correct salary structure based on regime.
* Comparison report: Old vs New regime tax deduction.

**Part 5 – Customization**

* Custom Doctype: Employee Investment Declaration
* Fields: Section 80C, Section 80D, Other Exemptions, Total Investment.

### 📸 Screenshots

### Part 1
**Job Applicant Workflow**
https://github.com/user-attachments/assets/89be2cec-1b0e-4464-b153-1ee381790169

**Custom source of application in field**
<img width="1710" height="760" alt="image" src="https://github.com/user-attachments/assets/5acd9988-e665-411b-b178-eae7ab7bb742" />

**Report and Chart showing applicants count grouped by Source of Application**

<img width="1658" height="579" alt="image" src="https://github.com/user-attachments/assets/74e2e240-53a2-4610-946a-d81847e645b1" />
###
<img width="1651" height="466" alt="image" src="https://github.com/user-attachments/assets/30b47051-8ee3-4e95-8716-a3c6f4966f07" />

### Part 2

**Employee Lifecycle Workflow**
https://github.com/user-attachments/assets/593310b4-e2d3-442e-b392-500d30ae7f9a

**Automations**
https://github.com/user-attachments/assets/31694819-aa37-42d5-ac60-957081dd1de5

**Experience Certificate Attachment**
https://github.com/user-attachments/assets/f73f9b9f-67b5-429f-8b15-cb57abac8006

### Part 3

**Salary Structure with earnings and deductions**
https://github.com/user-attachments/assets/b26b5738-e912-4965-bc4d-d7b39477dd65

**Payroll Entry for multiple employees**
https://github.com/user-attachments/assets/fcf8e4e6-1b66-4a20-bb1c-82bce98c4623

**Printformat with branding**
[brandedprintformat.pdf](https://github.com/user-attachments/files/22414162/brandedprintformat.pdf)


### Part 4

**Salary Structures: Old Regime & New Regime**
https://github.com/user-attachments/assets/48f899a4-8829-4304-bb84-0b6ad2f3788f

**Custom tax regime preference field**
<img width="1631" height="966" alt="image" src="https://github.com/user-attachments/assets/7e1b3706-64c5-4f2d-9d28-dc3b345bbbc8" />

**Tax comparison report**
<img width="1710" height="760" alt="image" src="https://github.com/user-attachments/assets/fd60115f-4f95-4b2f-a859-f20f94628db0" />

### Part 5











### License

mit
