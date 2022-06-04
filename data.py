import datetime as dt 
import pandas as pd 

from models import Appointment, Employee, Day


# employees = pd.read_csv("csvs/employees.csv")
# customers = pd.read_csv("csvs/customers.csv")


def get_appointments_on_date(date):
    #returns appointments on specified date
    appointments = pd.read_csv("csvs/appointments.csv", header=0)
    df = pd.DataFrame(appointments)
    return pd.DataFrame(appointments[appointments['date']==date])
    

def get_appointments_by_day():
    #returns Day object
    dict = {}
    days = []
    
    appointments = pd.read_csv("csvs/appointments.csv", header=0)
    df = pd.DataFrame(appointments)
    
    for index, a in df.iterrows():
        mapntmnt = Appointment(a['phone_no'], a['date'], a['slot'], a['activity'], a['first_name'], a['last_name'])
        
        try:
            dict[a['date']].append(mapntmnt)
        except KeyError:
            dict[a['date']] = [mapntmnt,]
            
    for day in dict:
        days.append(Day(day, dict[day]))
    return days

def get_appointment_summary():
    return get_appointments_by_day()


def get_employee_summary():
    res = []
    employees = pd.read_csv("csvs/employees.csv", header=0)
    df = pd.DataFrame(employees)

    for index, e in df.iterrows():
        emp = Employee(first_name=e['first_name'], last_name=e['last_name'], post=e['post'], id=e['id'])
        res.append(emp)
    return res

def get_employee(id, pw):
    employees = pd.read_csv("csvs/employees.csv", header=0)
    df = pd.DataFrame(employees)
    for index, e in df.iterrows():
        if e['id'] == id and e['password'] == pw:
            return Employee(first_name=e['first_name'], last_name=e['last_name'], post=e['post'], id=e['id'], password=e['password'])
    return None
    


def get_employee_by_id(id):
    employees = pd.read_csv("csvs/employees.csv", header=0)
    df = pd.DataFrame(employees)
    for index, e in df.iterrows():
        if e['id'] == id:
            return Employee(e['first_name'], e['last_name'], e['post'], e['id'], e['password'])
    return None

