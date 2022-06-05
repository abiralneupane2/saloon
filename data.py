import datetime as dt

import pandas as pd 



def get_appointments_on_date(date):
    #returns appointments on specified date
    appointments = pd.read_csv("csvs/appointments.csv", header=0)
    return pd.DataFrame(appointments[appointments['date']==date])
    

def get_appointments_by_day(date=str(dt.datetime.min)):
    #returns appointments sorted by day after specified date
    appointments = pd.read_csv("csvs/appointments.csv", header=0)
    df = pd.DataFrame(appointments[appointments['date'] >= date])
    df.sort_values(by='date')
    return df


def get_appointment_summary():
    #used by manager to get all appointments
    return get_appointments_by_day()


def get_employee_summary():
    #used by manager to get all employees
    employees = pd.read_csv("csvs/employees.csv", header=0)
    return pd.DataFrame(employees)


def login_employee(id, pw):
    #login employee
    employees = pd.read_csv("csvs/employees.csv", header=0)
    employees = employees[employees['id'] == id]
    employees = employees[employees['password'] == pw]
    if not employees.empty:
        return employees.iloc[0]
    
    return None



def delete_employee_from_csv(id):
    employees = pd.read_csv("csvs/employees.csv", header=0)
    employees = employees[employees['id'] == id]
    print(employees)
    input()
    try:
        if not employees.empty:
            employees.set_index('id')
            employees.drop(employees.query(f"id=={id}"))
            return True
    except:
        pass
    return False