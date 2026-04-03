# Payroll Management System (Python GUI)

A simple and user-friendly **Payroll Management System** built using **Python **.
This application allows users to manage employee records, calculate salaries, and generate payslips.

---

##  Features

*  Add Employee Details
*  View All Employees
*  Calculate Salary (HRA, DA, Tax)
*  Delete Employee
*  Real-time Payslip Display

---

##  Salary Calculation Logic

The system calculates salary using:

* **HRA (House Rent Allowance)** → 20% of Basic Salary
* **DA (Dearness Allowance)** → 10% of Basic Salary
* **Tax Deduction** → 5% of Basic Salary

**Net Salary = Basic + HRA + DA - Tax**

---

## Tech Stack

*  Python

---

##  Project Structure

```
payrollsystem/
│
├── main.py          # Main application file
├── README.md        # Project documentation
```

---

##  Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nagavardhan888/payrollsystem.git
cd payrollsystem
```

---

### 2️⃣ Install Requirements

Tkinter comes pre-installed with Python (usually).
If not:

```bash
pip install tk
```

---

## ▶ Running the Application

```bash
python payroll_gui.py
```

---


## Use Case

This project is useful for:

* Learning Python GUI development
* Understanding payroll calculations
* Academic mini-project submissions

---

##  Future Enhancements

* Database integration (SQLite / MongoDB)
* PDF Payslip generation
* Web-based version (React + Node.js)
* Authentication system

---
## Acknowledgements

Developed as a **micro project for learning and academic purposes**.

---
