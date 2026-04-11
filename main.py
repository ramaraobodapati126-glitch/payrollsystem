employees = []

def add_employee():
    name = input("Enter Name: ")
    emp_id = input("Enter ID: ")
    
    try:
        hours = float(input("Enter Hours Worked: "))
        rate = float(input("Enter Hourly Rate: "))
        bonus = float(input("Enter Bonus: "))
    except:
        print("Invalid input\n")
        return

    employee = {
        "name": name,
        "id": emp_id,
        "hours": hours,
        "rate": rate,
        "bonus": bonus
    }

    employees.append(employee)
    print("Employee added successfully!\n")


def view_employees():
    if not employees:
        print(" No employees found\n")
        return

    print("\n===== Employee List =====")
    for emp in employees:
        print(f"Name: {emp['name']}, ID: {emp['id']}, Hours: {emp['hours']}, Rate: {emp['rate']}")
    print()


def calculate_salary():
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp['id'] == emp_id:

            hours = emp['hours']
            rate = emp['rate']
            bonus = emp['bonus']
            if hours > 40:
                overtime_hours = hours - 40
                overtime_pay = overtime_hours * rate * 1.5
                base_pay = 40 * rate
            else:
                overtime_hours = 0
                overtime_pay = 0
                base_pay = hours * rate

            gross = base_pay + overtime_pay + bonus
            tax = gross * 0.10
            net_salary = gross - tax

            print("\n===== PAYSLIP =====")
            print(f"Employee Name : {emp['name']}")
            print(f"Employee ID   : {emp['id']}")
            print(f"Hours Worked  : {hours}")
            print(f"Hourly Rate   : {rate}")
            print(f"Base Pay      : {base_pay}")
            print(f"Overtime Pay  : {overtime_pay}")
            print(f"Bonus         : {bonus}")
            print(f"Tax (10%)     : {tax}")
            print("---------------------------")
            print(f"Net Salary    : {net_salary}\n")
            return

    print(" Employee not found\n")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")

    for emp in employees:
        if emp['id'] == emp_id:
            employees.remove(emp)
            print("Employee deleted successfully\n")
            return

    print(" Employee not found\n")


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


menu()
