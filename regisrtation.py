from string import digits
from string import ascii_uppercase
from string import ascii_lowercase
from string import ascii_letters

class Registration:
    def __init__(self, log, passw):
        self.login=log
        self.password=passw

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if not isinstance(value, str):
            raise TypeError
        if value.count("@")!=1:
            raise ValueError
        if '.' not in value or value[::-1].index('.')>value[::-1].index('@'):
            raise ValueError
        self.__login=value

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_digit(new_p):
        for i in digits:
            if i in new_p:
                return True
        return False

    @staticmethod
    def is_include_all_register(new_p):
        c=0
        for i in ascii_uppercase:
            if i in new_p:
                c+=1
                break
        for j in ascii_lowercase:
            if j in new_p:
                c+=1
                break
        return True if c==2 else False

    @staticmethod
    def is_include_only_latin(new_p):
        for i in new_p:
            if i not in ascii_letters:
                if i not in digits:
                    return False
                    break
        return True

    @staticmethod
    def check_password_dictionary(new_p):
        if new_p in open(r'easy_passwords.txt').read():
            return True
        else:
            return False



    @password.setter
    def password(self, new_p):
        if not isinstance(new_p,str):
            raise TypeError("Password must be a string")
        if len(new_p)<5 or len(new_p)>11:
            raise ValueError('Password must be from 4 to 12 units long')
        if not Registration.is_include_digit(new_p):
            raise ValueError('Password must contain at least one letter')
        if not Registration.is_include_all_register(new_p):
            raise ValueError('Password must contain upper and lower case')
        if not Registration.is_include_only_latin(new_p):
            raise ValueError('Please use English')
        if Registration.check_password_dictionary(new_p):
            raise ValueError('Your password is too easy')
        self.__password=new_p