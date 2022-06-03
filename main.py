import datetime as dt


from models import Employee, Appointment, Customer
from data import get_appointments_on_date, get_appointments_by_day

def set_appointment():
    is_new = input("Is the customer new?(Y/N): ")
    customer_id = ''
    if is_new =="n":
        customer_id = input("Enter phone no: ")
    if customer_id == '':
        first_name = input("First name: ")
        last_name = input("Last name: ")
        customer_id = input("Phone number: ")
    customer = Customer(first_name, last_name, customer_id)
    
    while True:
        try:
            print("When should I set appointment?")
            day = input("0:Today\t1:Tomorrow\n2:After 2 days\t3:After 3 days\n...\n")
            day = dt.date.today()+dt.timedelta(days=int(day))
            appointments = get_appointments_on_date(day)
            print(appointments)
            
            break
        except ValueError as e:
            print("Provide proper value.", str(e))

    slot = input("Enter the time of appointment: ")
    type = input("Enter activity.(Default haircut): ")
    a = Appointment(customer_id, day, slot, type)
    a.save()
    input("Appointment create successfully. Press enter to continue.")
    

    
    

def view_appointments():
    days = get_appointments_by_day()
    
    for day in days:
        print(day.date)
        for app in day.slot_list:
            print(app.customer_id, app.slot)
    input("Press enter to continue.")

def delete_appointment():
    pass


def reception(receptionist):
    
    while True:
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
        
def manager(manager):
    pass


if __name__ == '__main__':
    e = Employee("Abiral", "Neupane", "r", "rec-1")
    reception(e)

