import datetime as dt 
import pandas as pd 

from .models import Appointment, Employee, Customer

appointments = pd.read_csv("appointments.csv")
employees = pd.read_csv("employees.csv")
customers = pd.read_csv("customers.csv")



