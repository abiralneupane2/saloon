import argparse
import datetime as dt

import pandas as pd





parser = argparse.ArgumentParser()
parser.add_argument("-a", "--createappointmentcsv", help="create initial csv file to store appointments", action="store_true")
parser.add_argument("-e", "--createemployee", help="create employee of provided post", choices=['r','m'])
args = parser.parse_args()

# if args.createappointmentcsv:
#     dict = {
#         'date': [],
#         'day': [],
#         'time': [],
#     }
#     for i in range(8):
#         dict[f"appointment_{i}"] = []
#     df = pd.DataFrame(dict)
#     df.to_csv("csvs/appointments.csv", sep="\t", index=False)
    

if args.createemployee:
    print("employee created")



