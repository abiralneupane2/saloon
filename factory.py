import argparse

import pandas as pd

from .models import Employee, Appointment


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--createappointmentcsv", help="create initial csv file to store appointments", action="store_true")
parser.add_argument("-e", "--createemployee", help="create employee of provided post", choices=['r','m'])
args = parser.parse_args()

if args.createappointmentcsv:
    print("csv created")

if args.createemployee:
    print("employee created")



