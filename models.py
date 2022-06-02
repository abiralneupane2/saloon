import pandas as pd

class Person:
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Employee(Person):
    def __init__(self, first_name, last_name, post, id):
        super().__init__(first_name, last_name)
        self.post = post
        self.id = id

class Customer(Person):
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name)
        self.id = id

class Appointment:
    def __init__(self, customer_id, date, slot, _type='haircut'):
        self.customer_id = customer_id
        self.date = date
        self._type = _type
        self.slot = slot
    
    def save(self):
        df = pd.DataFrame(self.to_dict)
        df.to_csv("csvs/appointments.csv", mode='a', index=False, header=False)

    def to_dict(self):
        return {
            'date':self.date,
            'slot':self.slot,
            'type':self._type,
            'customer_id':self.customer_id
        }

class Day:
    
    def __init__(self, date, slot_list):
        self.date = date
        self.slot_list = slot_list
    
    




    
    