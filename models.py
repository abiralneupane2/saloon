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
    
    def to_dict(self):
        return {
            'phone_no': self.id,
            'first_name': super().first_name,
            'last_name': super().last_name,
        }
    def save(self):
        df = pd.DataFrame([self.to_dict()])
        df.to_csv("csvs/customers.csv", mode='a', header=False, index=False)

class Appointment:
    def __init__(self, customer_id, date, slot, _type):
        self.customer_id = customer_id
        self.date = date
        self._type = _type or 'haircut'
        self.slot = slot
    
    def save(self):
        df = pd.DataFrame([self.to_dict()])
        df.to_csv("csvs/appointments.csv", mode='a', header=False, index=False)

    def to_dict(self):
        return {
            'date':self.date,
            'customer_id':self.customer_id,
            'slot':self.slot,
            'type':self._type,
            
        }

class Day:
    
    def __init__(self, date, slot_list):
        self.date = date
        self.slot_list = slot_list
    
    




    
    