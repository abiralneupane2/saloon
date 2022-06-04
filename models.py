import pandas as pd



class Employee:
    def __init__(self, first_name, last_name, post, id, password=None):
        
        self.first_name = first_name
        self.last_name = last_name
        self.post = post
        self.id = id
        self.password = password

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'post': self.post,
            'password': self.password
        }
    def save(self):
        df = pd.DataFrame([self.to_dict()])
        df.to_csv("csvs/employees.csv", mode='a', header=False, index=False)
    
    def delete(self):
        employees = pd.read_csv("csvs/employees.csv", header=0, index='id')
        employees.drop('self.id')



class Appointment:
    def __init__(self, phone_no, date, slot, _type, first_name, last_name):
        self.phone_no = phone_no
        self.date = date
        self._type = _type or 'haircut'
        self.slot = slot
        self.first_name = first_name
        self.last_name = last_name
    
    def save(self):
        df = pd.DataFrame([self.to_dict()])
        df.to_csv("csvs/appointments.csv", mode='a', header=False, index=False)

    def to_dict(self):
        return {
            'date':self.date,
            'phone_no':self.phone_no,
            'slot':self.slot,
            'type':self._type,
            'first_name':self.first_name,
            'last_name':self.last_name
            
        }

class Day:
    
    def __init__(self, date, slot_list):
        self.date = date
        self.slot_list = slot_list
    
    




    
    