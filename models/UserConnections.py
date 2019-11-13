#!/usr/bin/python3
"""
This sets all the attributes for the UserConnections class
"""
from '../gettingdata.py' import UserData


class UserConnections:
    """
    Setting how to handle attributes and printing
    """

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """
        This section handles how to print the attributes of the class
        """
        initialUsernameData = {}
        initialUsernameData['initial_member'] = self.username
        initialUsernameData['data'] = UserData(self.username)
        initialUsernameData['candidates'] = self.candidates
        final_list = [initial_member, data, candidates]
        return (final_list)
