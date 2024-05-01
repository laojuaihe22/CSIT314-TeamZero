
from flask_login import UserMixin

class User:
     def __init__(self, email, password):
        self.email = email
        self.password = password
