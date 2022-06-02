import datetime as dt 
import pandas as pd 

from models import Appointment, Employee, Customer, Day


# employees = pd.read_csv("csvs/employees.csv")
# customers = pd.read_csv("csvs/customers.csv")


def get_appointments_on_date(date):
    appointments = pd.read_csv("csvs/appointments.csv", header=0)
    df = pd.DataFrame(appointments)
    apps = df['date']==date
    return apps
    # appointment_objects = []
    # for a in apps:
    #     appointment_objects.append(Appointment(a['customer_id'], a['date'], a['slot'], a['type']))
    # return appointment_objects

def get_appointments_by_day(date=None):
    dict = {}
    days = []
    if date is None:
        appointments = pd.read_csv("csvs/appointments.csv", header=0)
        df = pd.DataFrame(appointments)
        appointment_objects = []
        
        for index, a in df.iterrows():
            mapntmnt = Appointment(a['phone_no'], a['date'], a['slot'], a['activity'])
            try:
                dict[a['date']].append(mapntmnt)
            except KeyError:
                dict[a['date']] = [mapntmnt,]
    for day in dict:
        days.append(Day(day, dict[day]))
    return days



