import argparse
import datetime as dt

import pandas as pd





parser = argparse.ArgumentParser()
parser.add_argument("-e", "--createemployee", help="create employee of provided post", choices=['r','m'])
args = parser.parse_args()


    

if args.createemployee:
    print("employee created")

