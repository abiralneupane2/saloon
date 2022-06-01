class Person:
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Employee(Person):
    def __init__(self, first_name=None, last_name=None, post, id):
        super().__init__(first_name, last_name)
        self.post = post
        self.id = id

class Customer(Person):
    def __init__(self, first_name=None, last_name=None, id):
        super().__init__(first_name, last_name)
        self.id = id

class Appointment:
    def __init__(self, customer_id, datetime, _type):
        self.customer_id = customer_id
        self.datetime = datetime
        self._type = _type



    
    