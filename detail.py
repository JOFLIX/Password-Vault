import pyperclip


class Detail:

    """
    Class that generates new instances of details.
    """

    detail_list = []  # Empty detail list

    def __init__(self, user_name, account_name, number, email):

      # docstring removed for simplicity

        self.user_name = user_name
        self.account_name = account_name
        self.phone_number = number
        self.email = email

# detail_list = [] # Empty detail list
 # Init method up here
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

    # def delete_details():
    #     '''
    #     delete_detail method deletes a saved detail from the detail_list
    #     '''

    #     detail.detail_list.remove()

    @classmethod
    def find_by_number(cls, number):
        '''
        Method that takes in a number and returns a detail that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            detail of person that matches the number.
        '''

        for detail in cls.detail_list:
            if detail.phone_number == number:
                return detail

    @classmethod
    def detail_exist(cls, number):
        '''
        Method that checks if a detail exists from the detail list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the detail exists
        '''
        for detail in cls.detail_list:
            if detail.phone_number == number:
                    return True

        return False

    @classmethod
    def display_details(cls):
        '''
        method that returns the detail list
        '''
        return cls.detail_list


# ......................
    @classmethod
    def copy_email(cls,number):
        detail_found = Detail.find_by_number(number)
        pyperclip.copy(detail_found.email)

    @classmethod
    def delete_details(cls):

        '''
        method that returns the detail list
        '''
        return cls.detail_list
