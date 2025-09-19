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
bench build --app girman_developer_assignment
bench clear-cache
bench --site your-site-name migrate
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
* Fields: Employee, Section 80C, Section 80D, Other Exemptions.
* Link this to Payroll so that tax calculations consider these declarations.

### 📸 Screenshots

**Part 1**

**Job Applicant Workflow**

![jobapplicant_workflow](https://github.com/user-attachments/assets/af863986-0ae4-4952-a048-782660b75ca3)

**Custom source of application in field**

<img width="1710" height="760" alt="image" src="https://github.com/user-attachments/assets/5acd9988-e665-411b-b178-eae7ab7bb742" />

**Report and Chart showing applicants count grouped by Source of Application**

**CHART**

<img width="1658" height="579" alt="image" src="https://github.com/user-attachments/assets/74e2e240-53a2-4610-946a-d81847e645b1" />

**REPORT**

<img width="1651" height="466" alt="image" src="https://github.com/user-attachments/assets/30b47051-8ee3-4e95-8716-a3c6f4966f07" />

### Part 2

**Employee Lifecycle Workflow**

![emplifecyclewf](https://github.com/user-attachments/assets/4bee9406-67e0-4162-b51a-97ad5387ea3d)

**Automations**

![statusautomation](https://github.com/user-attachments/assets/2bfa0105-82b3-4351-93e6-27ad2613bcb1)

**Experience Certificate Attachment**

![Expcerti](https://github.com/user-attachments/assets/6e637a4b-75c6-474a-b2ed-a261032d48f9)


### Part 3

**Salary Structure with earnings and deductions**

![structureE D](https://github.com/user-attachments/assets/323057bf-e2fd-457d-9bb3-54a838a62149)


**Payroll Entry for multiple employees**

![multEmp](https://github.com/user-attachments/assets/fb76adcc-6a73-4ea6-8847-ef09a54d4cfb)


**Printformat with branding(Print Screen)**

<img width="1900" height="944" alt="image" src="https://github.com/user-attachments/assets/d74ae721-8741-4d94-8d26-0fe95bd22c27" />

### Part 4

**Salary Structures: Old Regime & New Regime**

![old_new](https://github.com/user-attachments/assets/c56cd78f-31d2-4753-a064-a35e66bcb3ef)

**Custom tax regime preference field**

<img width="1631" height="966" alt="image" src="https://github.com/user-attachments/assets/7e1b3706-64c5-4f2d-9d28-dc3b345bbbc8" />

**Tax comparison report**

<img width="1710" height="760" alt="image" src="https://github.com/user-attachments/assets/fd60115f-4f95-4b2f-a859-f20f94628db0" />

### Part 5

**Employee Investment Declaration**
<img width="1900" height="944" alt="image" src="https://github.com/user-attachments/assets/c33ff117-915d-460b-b2c5-e121a733ffe4" />

**Payroll tax calculations**
<img width="1900" height="944" alt="image" src="https://github.com/user-attachments/assets/a51c0e69-4db4-47e6-af5b-70db8431b155" />





### 👨‍💻 Author

**Sivanesh V J**

**Frappe Developer Assignment Submission**

**Email: sivanesh2251@gmail.com**

### License

mit
