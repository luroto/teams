#!/usr/bin/python3
"""
This file sets all about UserData class
"""


class UserData:
    """ This class sets all the attributes required by bios petition"""

    def __init__(self, *args, **kwargs):
        """ Instatiation for a petition. key=value arguments are expected"""""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """ Setting how the userdata will print"""
        userdata = {}
        userdata['public_id'] = self.public_id
        userdata['fullname'] = self.fullname
        userdata['professionalHeadline'] = self.professionalHeadline
        userdata['skills'] = self.skills
        return (userdata)
