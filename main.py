import datetime as dt
import os

from data import get_appointments_on_date, get_appointments_by_day, get_appointment_summary, get_available_workers, get_employee_summary, login_employee, delete_employee_from_csv, save_appointment_to_csv, save_employee_to_csv, get_available_workers, get_weekly_roaster

def set_appointment():
    os.system('cls||clear')
    print("Set appointment.")
    
    
    
    while True:
        try:
            print("When should I set appointment?")
            day = input("0:Today\t1:Tomorrow\n2:After 2 days\t3:After 3 days\n...\n")
            if day == 'back':
                return
            day = dt.date.today()+dt.timedelta(days=int(day))
            appointments = get_appointments_on_date(str(day))
            print("Appointments set: ")
            if appointments.empty:
                print("No appointments set till now")
            else:
                print(appointments)
            print("Available workers:")
            workers = get_available_workers(day)
            if workers is not None:
                print(workers)
                break
            else:
                print("No one is available")
                input()
            
        except ValueError as e:
            print("Provide proper value.", str(e))
    appointed_to = input("Which worker should serve?")
    slot = input("Enter the time of appointment: ")
    type = input("Enter activity.(Default haircut): ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_no = input("Phone number: ")
    save_appointment_to_csv(day, phone_no, slot, type, first_name, last_name, appointed_to)
    input("Appointment create successfully. Press enter to continue.")
    

    
    

def view_appointments():
    os.system('cls||clear')
    days = get_appointments_by_day(str(dt.date.today()))
    print(days)
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
    e = save_employee_to_csv(first_name, last_name, post, id, password)
    e.save()
    input("Employee added successfully. Press enter to continue.")

def view_employee_summary():
    os.system('cls||clear')
    print("Employee summary.")
    employees = get_weekly_roaster()
    print(employees)
    input("Press enter to continue")

def view_appointment_summary():
    os.system('cls||clear')
    print("Appointment summary.")
    days = get_appointments_by_day()
    print(days)
    input("\nPress enter to continue.")

def delete_employee():
    os.system('cls||clear')
    id = input("Enter id of employee to delete: ")
    if delete_employee_from_csv(id):
        input("Deleted employee successfully. Press enter to continue.")
    input("Employee not found. Press enter to continue.")
    


def manager(manager):
   #manager table
    while True:
        os.system('cls||clear')
        print(f"Welcome, {manager.first_name}. What do you want to do?")
        inp = input("1:View appointment summary\n2:View employee summary\n3:Add employee\n4:Delete employee\n5:Logout\n")
        if inp == '1':
            view_appointment_summary()
        elif inp == '2':
            view_employee_summary()
        elif inp == '3':
            add_employee()
        elif inp == '4':
            delete_employee()
        elif inp == '5':
            os.system('cls||clear')
            break
        else:
            print("Give valid input.")


def reception(receptionist):
    #receptionist table
    while True:
        os.system('cls||clear')
        print(f"Welcome, {receptionist.first_name}\n1.Set an appointment\n2.View all appointments\n3.Delete an appointment\n4.Logout\n")
        inp = input("Enter a value {1,2,3,4}\n")
        if inp=="1":
            set_appointment()
        elif inp=="2":
            view_appointments()
        elif inp=="3":
            print("delete")
        elif inp == '4':
            os.system('cls||clear')
            break
        else:
            print("Invalid choice. try again.\n")



if __name__ == '__main__':
    os.system('cls||clear')
    print("Login")
    while True:
        #loop until right credentials is provided
        id = input("Enter your id: ")
        pw = input("Enter your password: ")
        e = login_employee(id, pw)
        if e is not None:
            break
        print("Enter valid id and password.")

    if e.post == 'r':
        reception(e)
    if e.post == 'm':
        manager(e)

