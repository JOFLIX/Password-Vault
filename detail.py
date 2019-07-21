
import pyperclip
import random
import string
import sys

import random
import string
import sys


class Detail:
    """
    Class that generates new cases of details.
    """

    detail_list = []  # Empty detail list

    def __init__(self, user_name, account_name,password,email):

      # docstring removed for simplicity

        self.user_name = user_name
        self.account_name = account_name
        self.account_password = password
        self.email = email

# detail_list = [] # Empty detail list
 # Init method up here
    # def password(self,length):
    #     """Generate a random password."""
    #     alphabet = string.ascii_letters + string.digits
    
    def save_detail(self):
        '''
        save_detail method saves detail objects into detail_list
        '''

        Detail.detail_list.append(self)

    def delete_detail(self):
        '''
        delete_detail method deletes a saved detail from the detail_list
        '''

        Detail.detail_list.remove(self)

    # def generate_password(self):

    #     """
    #     a method that gnerates pasword using choice and random key words
    #     """
    #     Detai.detail.join(random.choice(alphabet) for i in range(length))



        
    @classmethod
    def find_by_password(cls, password):
        '''
        Method that takes in a password and returns a detail that matches that password.

        Args:
            password: account password to search for
        Returns :
            detail of person that matches the password.
        '''

        for detail in cls.detail_list:
            if detail.account_password == password:
                return detail

    @classmethod
    def detail_exist(cls, password):
        '''
        Method that checks if a detail exists from the detail list.
        Args:
            password: account password to search if it exists
        Returns :
            Boolean: True or false depending if the detail exists
        '''
        for detail in cls.detail_list:
            if detail.account_password == password:
                    return True

        return False

    @classmethod
    def display_details(cls):
        '''
        method that returns the detail list
        '''
        return cls.detail_list

    def passsword(self,length):
        """Generate a random password."""
        alphabet = string.ascii_letters + string.digits
        while True:
            pw = ''.join(random.choice(alphabet) for i in range(length))
            if (any(c.islower() for c in pw)
                    and any(c.isupper() for c in pw)
                    and any(c.isdigit() for c in pw)):
                break
        return(pw)
# ......................
    @classmethod
    def copy_email(cls,password):
        detail_found = Detail.find_by_password(password)
        pyperclip.copy(detail_found.email)

    @classmethod
    def delete_details(cls):

        '''
        method that returns the detail list
        '''
        return cls.detail_list


