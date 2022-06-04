import datetime as dt
import os

from models import Employee, Appointment
from data import get_appointments_on_date, get_appointments_by_day, get_appointment_summary, get_employee_summary, get_employee, get_employee_by_id

def set_appointment():
    os.system('cls||clear')
    print("Set appointment.")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_no = input("Phone number: ")
    
    
    while True:
        try:
            print("When should I set appointment?")
            day = input("0:Today\t1:Tomorrow\n2:After 2 days\t3:After 3 days\n...\n")
            if day == 'back':
                return
            day = dt.date.today()+dt.timedelta(days=int(day))
            appointments = get_appointments_on_date(str(day))
            print(appointments)
            
            break
        except ValueError as e:
            print("Provide proper value.", str(e))

    slot = input("Enter the time of appointment: ")
    type = input("Enter activity.(Default haircut): ")
    a = Appointment(phone_no, day, slot, type, first_name, last_name)
    a.save()
    input("Appointment create successfully. Press enter to continue.")
    

    
    

def view_appointments():
    os.system('cls||clear')
    days = get_appointments_by_day()
    
    for day in days:
        print(day.date)
        for app in day.slot_list:
            print(app.phone_no, app.first_name, app.last_name, app.slot)
    input("Press enter to continue.")

def delete_appointment():
    pass



        


def add_employee():
    os.system('cls||clear')
    print("Add Employee")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    password = input("Enter password: ")
    post = input("Enter post.\nr : Receptionist\tm : Manager")
    id = input("Enter id for user: ")
    e = Employee(first_name, last_name, post, id, password)
    e.save()
    input("Employee added successfully. Press enter to continue.")

def view_employee_summary():
    os.system('cls||clear')
    print("Employee summary.")
    employees = get_employee_summary()
    for employee in employees:
        print("id: ", employee.id, "name: ", employee.first_name, employee.last_name, "post: ", employee.post)
    input("Press enter to continue")

def view_appointment_summary():
    os.system('cls||clear')
    print("Appointment summary.")
    days = get_appointments_by_day()

    for day in days:
        print(day.date)
        for app in day.slot_list:
            print("phone: ", app.phone_no, "name: ", app.first_name, app.last_name, "time: ", app.slot)
    input("\nPress enter to continue.")

def delete_employee():
    os.system('cls||clear')
    id = input("Enter id of employee to delete")
    e = get_employee_by_id(id)
    if e is not None:
        e.delete()
        input("Employee deleted. Press enter to continue.")
        return
    input("Employee not found. Press enter to continue.")
    


def manager(manager):
   
    while True:
        os.system('cls||clear')
        print(f"Welcome, {manager.first_name}. What do you want to do?")
        inp = input("1:View appointment summary\n2:View employee summary\n3:Add employee\n")
        if inp == '1':
            view_appointment_summary()
        elif inp == '2':
            view_employee_summary()
        elif inp == '3':
            add_employee()
        elif inp == '4':
            delete_employee()
        else:
            print("Give valid input.")


def reception(receptionist):
    
    while True:
        os.system('cls||clear')
        print(f"Welcome, {receptionist.first_name}\n1.Set an appointment\n2.View all appointments\n3.Delete an appointment\n4.View available appointments\n")
        inp = input("Enter a value {1,2,3,4}\n")
        if inp=="1":
            set_appointment()
        elif inp=="2":
            view_appointments()
        elif inp=="3":
            print("delete")
        else:
            print("Invalid choice. try again.\n")



if __name__ == '__main__':
    os.system('cls||clear')
    print("Login")
    while True:
        id = input("Enter your id: ")
        pw = input("Enter your password: ")
        e = get_employee(id, pw)
        if e is not None:
            break
        print("Enter valid id and password.")
    if e.post == 'r':
        reception(e)
    if e.post == 'm':
        manager(e)

