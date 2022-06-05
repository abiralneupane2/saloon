import datetime as dt
from turtle import pos

import pandas as pd 
import numpy as np



def get_appointments_on_date(date):
    #returns appointments on specified date
    appointments = pd.read_csv("appointments.csv", header=0)
    return pd.DataFrame(appointments[appointments['date']==date])
    

def get_appointments_by_day(date=str(dt.datetime.min)):
    #returns appointments sorted by day after specified date
    appointments = pd.read_csv("appointments.csv", header=0)
    df = pd.DataFrame(appointments[appointments['date'] >= date])
    df.sort_values(by='date')
    return df


def get_appointment_summary():
    #used by manager to get all appointments
    return get_appointments_by_day()


def get_employee_summary():
    #used by manager to get all employees
    employees = pd.read_csv("employees.csv", header=0)
    return pd.DataFrame(employees)


def login_employee(id, pw):
    #login employee
    employees = pd.read_csv("employees.csv", header=0)
    employees = employees[employees['id'] == id]
    employees = employees[employees['password'] == pw]
    if not employees.empty:
        return employees.iloc[0]
    
    return None



def delete_employee_from_csv(id):
    #delete employee
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

def save_appointment_to_csv(date, phone_no, slot, type, first_name, last_name,appointed_to):
    #save appointment
    df = pd.DataFrame([{
        'date':date,
        'phone_no':phone_no,
        'slot':slot,
        'type':type or "haircut",
        'first_name':first_name,
        'last_name':last_name,
        'appointed_to':appointed_to
    }])
    df.to_csv("appointments.csv", mode='a', header=False, index=False)

def save_employee_to_csv(first_name, last_name, post, id, password):
    df = pd.DataFrame([{
        'id': id,
        'first_name': first_name,
        'last_name': last_name,
        'post': post,
        'password': password
    }])
    df.to_csv("employees.csv", mode='a', header=False, index=False)

def get_available_workers(date):
    roaster = pd.read_csv("weekly_roaster.csv",header=0)
    weekday = date.weekday()
    try:
        roaster = roaster[roaster[str(weekday)] != "0"]
        return roaster[['name',str(weekday)]]
    except:
        return None