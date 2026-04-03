employees = []
def add_employee():
    name = input("Enter Name: ")
    emp_id = input("Enter ID: ")
    try:
        basic = float(input("Enter Basic Salary: "))
    except:
        print("Invalid salary input")
        return
    employee = {
        "name": name,
        "id": emp_id,
        "basic": basic
    }
    employees.append(employee)
    print(" Employee added successfully!\n")
def view_employees():
    if not employees:
        print(" No employees found\n")
        return
    print("\n===== Employee List =====")
    for emp in employees:
        print(f"Name: {emp['name']}, ID: {emp['id']}, Salary: {emp['basic']}")
    print()
def calculate_salary():
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp['id'] == emp_id:
            basic = emp['basic']
            hra = basic * 0.2
            da = basic * 0.1
            tax = basic * 0.05

            net_salary = basic + hra + da - tax

            print("\n===== PAYSLIP =====")
            print(f"Employee Name : {emp['name']}")
            print(f"Employee ID   : {emp['id']}")
            print(f"Basic Salary  : {basic}")
            print(f"HRA (20%)     : {hra}")
            print(f"DA (10%)      : {da}")
            print(f"Tax (5%)      : {tax}")
            print("---------------------------")
            print(f"Net Salary    : {net_salary}\n")
            return

    print(" Employee not found\n")
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")

    for emp in employees:
        if emp['id'] == emp_id:
            employees.remove(emp)
            print(" Employee deleted successfully\n")
            return

    print(" Employee not found\n")


# 📋 Menu
def menu():
    while True:
        print("===== Payroll Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Calculate Salary")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            calculate_salary()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print(" Exiting program...")
            break
        else:
            print(" Invalid choice\n")


# ▶️ Run Program
menu()