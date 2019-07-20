#!/usr/bin/env python3.6
from detail import Detail
import pyperclip
######Create functions to implement what the behaviours we have created####


def create_detail(fname, lname, phone, email):
    """
    Function to create a new detail

    """
    new_detail = Detail(fname, lname, phone, email)
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


def find_detail(number):
    """
    Function that finds a detail by number and returns the detail
    """
    return Detail.find_by_number(number)

### We create a func that takes in a number and calls the Detail class method find_by_number that returns the detail. ###

### Check if a detail exists ###


def check_existing_details(number):
    """
    Function that check if a detail exists with that number and return a Boolean
    """
    return Detail.detail_exist(number)

### The function check_existing_details takes in a number as an argument and calls the class method detail_exist which returns a boolean.###

## Displaying all details ##


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
def copy_email(cls, number):
    """
    A funct that copies the email using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    detail_found = Detail.find_by_number(number)
    pyperclip.copy(detail_found.email)


def main():
    print("Hello Welcome to your detail list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print(
                        "Use these short codes : Un - create a new user account, dc - display details, fc -find a detail, ex -exit the detail list , del -delete detail, del-A -Delete all")

                    short_code = input().lower()

                    if short_code == 'Un':
                            print("New Detail")
                            print("-"*10)

                            print("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()

                            # create and save new Detail.
                            save_details(create_detail(
                                f_name, l_name, p_number, e_address))
                            print('\n')
                            print(f"New detail {f_name} {l_name}  created")
                            print('\n')

                    elif short_code == 'dc':

                            if display_details():
                                    print("Here is a list of all your details")
                                    print('\n')

                                    for detail in display_details():
                                            print(
                                                f"{detail.first_name} {detail.last_name} {e_address} {detail.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print(
                                        "You dont seem to have any details saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_details(search_number):
                                    search_detail = find_detail(
                                        search_number)
                                    print(
                                        f"{search_detail.first_name} {search_detail.last_name}")
                                    print('-' * 20)

                                    print(
                                        f"Phone number.......{search_detail.phone_number}")
                                    print(
                                        f"Email address.......{search_detail.email}")
                            else:
                                    print("That detail does not exist")

                    elif short_code == "del":
                         print("Enter the number of the detail you want to delete")
                         search_number = input()
                         if check_existing_details(search_number):
                             search_detail = find_detail(search_number)
                             print(
                                 f"{search_detail.first_name} {search_detail.last_name}")
                             print("_"*20)
                             detail.delete_detail()
                        #  if detail.delete_detail():
                             print('\n')
                             print(
                                 f'{f_name} {e_address} Successfully deleted!!')
                             print('\n')

                    elif short_code == 'del-A':

                            if delete_details():
                                    print("Here is a list of all your details")
                                    print('\n')

                                    for detail in delete_details():
                                            print(
                                                f"{detail.first_name} {detail.last_name} {e_address} {detail.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print(
                                        "You dont seem to have any details saved yet")
                                    print('\n')
                    elif short_code == "ex":
                                print("Bye .......")
                                break
                    else:
                            print(
                                "I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
