#!/usr/bin/env python3.6
from detail import Detail
# from password_gen import Generator
import pyperclip
import random
import string
import sys
######Create functions to implement what the behaviours we have created####


def create_detail(u_name, lname, account, email):
    """
    Function to create a new detail

    """
    new_detail = Detail(u_name, lname, account, email)
    return new_detail

###We create a function called create_detail(), that takes in four arguments###

#####Save details #####


def save_details(detail):
    """
    Function to save detail
    """
    detail.save_detail()

### we create save detail function that takes in a detail object and then calls the save_detail method to save the detail. ####

#####Delete Detail


def del_detail(detail):
    """
    Function to delete a detail

    """
    detail.delete_detail()

### We create a del_detail function that takes in a detail object and then calls the delete_detail() method on the detail object deleting it from the detail list####

##Fininding a detail ##


def find_detail(password):
    """
    Function that finds a detail by password and returns the detail
    """
    return Detail.find_by_password(password)

### We create a func that takes in a password and calls the Detail class method find_by_password that returns the detail. ###

### Check if a detail exists ###


def check_existing_details(password):
    """
    Function that check if a detail exists with that password and return a Boolean
    """
    return Detail.detail_exist(password)

### The function check_existing_details takes in a password as an argument and calls the class method detail_exist which returns a boolean.###

## Displaying all details ##
def passsword(length):
    """Generate a random password."""
    alphabet = string.ascii_letters + string.digits
    while True:
        pw = ''.join(random.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in pw)
                and any(c.isupper() for c in pw)
                and any(c.isdigit() for c in pw)):
            break
    return(pw)

def display_details():
    """
    Func that rteturns all the saved details

    """
    return Detail.display_details()
### Deleting details ####
@classmethod
def delete_details():
    """
    Func that rteturns all the saved details

    """
    return Detail.delete_details()


## Copy Email ##
#**********************#


@classmethod
def copy_email(cls, password):
    """
    A funct that copies the email using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    detail_found = Detail.find_by_password(password)
    pyperclip.copy(detail_found.email)


def main():
    print('Your secret word is used to access this vault.')
    print("Hello Welcome to your password vault. What is your secret word?")
    user_name = input()
    print("="*62)
    print(f"Hello {user_name}. How do we help you?")
    print('\n')

    while True:
                    print(
                        "Use these short codes to specify how you we may help you : un - create a new user account, dd - display details, fd -find an account detail, exit() -exit the detail list , del -delete detail, clear() -Delete all, To generate password run this command on your terminal: $ python3.6 password_gen.py")

                    short_code = input().lower()

                    if short_code == 'un':
                            print("New User Acccount")
                            print("="*71)

                            print("Enter registered account user name ....")
                            f_name = input()

                            print("Enter account name(eg. Facebook, WhatsApp)")
                            account_name = input()

                            print("Enter Password")
                            p_password = input()

                            print("Email address or account password used to register the account ...")
                            e_address = input()

                            # create and save new Detail.
                            save_details(create_detail(
                                f_name, account_name, p_password, e_address))
                            print('\n')
                            print(f"New detail {f_name} {account_name}  created")
                            print('\n')

                    elif short_code == 'dd':

                            if display_details():
                                    print("Here is a list of all your details")
                                    print('\n')

                                    for detail in display_details():
                                            print(
                                                f"{detail.user_name} {detail.account_name} {e_address} {detail.account_password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print(
                                        "You dont seem to have any details saved yet")
                                    print('\n')

                    elif short_code == 'fd':

                            print("Enter the password you want to search for")

                            search_password = input()
                            if check_existing_details(search_password):
                                    search_detail = find_detail(
                                        search_password)
                                    print(
                                        f"{search_detail.user_name} {search_detail.account_name}")
                                    print('=' * 80)

                                    print(
                                        f"account password.......{search_detail.account_password}")
                                    print(
                                        f"Email address.......{search_detail.email}")
                            else:
                                    print("That detail does not exist")

                    elif short_code == "del":
                         print("Enter the password of the detail you want to delete")
                         search_password = input()
                         if check_existing_details(search_password):
                             search_detail = find_detail(search_password)
                             print(
                                 f"{search_detail.user_name} {search_detail.account_name}")
                             print("_"*20)
                             detail.delete_detail()
                        
                             print('\n')
                             print(
                                 f'{f_name} {e_address} Successfully deleted!!')
                             print('\n')

                    elif short_code == 'clear()':

                            if delete_details():
                                    print("Here is a list of all your details")
                                    print('\n')

                                    for detail in delete_details():
                                            print(
                                                f"{detail.user_name} {detail.account_name} {e_address} {detail.account_password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print(
                                        "You dont seem to have any account details saved yet")
                                    print('\n')
                    elif short_code == "exit()":
                                print("Safely secured!!")

# def password(length):
#     """Generate a random password."""
#     alphabet = string.ascii_letters + string.digits
#     while True:
#         pw = ''.join(random.choice(alphabet) for i in range(length))
#         if (any(c.islower() for c in pw)
#                 and any(c.isupper() for c in pw)
#                 and any(c.isdigit() for c in pw)):
            
#     return(pw)
                                break
                    else:
                            print(
                                "I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
