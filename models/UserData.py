#!/usr/bin/python3
"""
This file sets all about UserData class
"""


class UserData:
    """ This class sets all the attributes required by bios petition"""

    def __init__ (self, *args, **kwargs):
        """ Instatiation for a petition. key=value arguments are expected"""""
        if (kwargs):
            self.public_Id = kwargs['public_Id']
            self.fullname = kwargs['fullname']
            self.professionalHeadline = kwargs['professionalHeadline']
            self.skills = kwargs['skills']
            if 'photo_url' in kwargs:
                self.photo_url = kwargs['photo_url']
        else:
            self.public_Id = ""
            self.fullname = ""
            self.professionalHeadline = ""
            self.skills = []
   
    def __str__(self):
        """ Setting how the userdata will print"""
        if self.photo_url:
            return ("{{ '{}': '{}', '{}': '{}', '{}': '{}', {}: {}, {}: {} }}".format('public_Id', self.public_Id, 'fullname', self.fullname, 'professionalHeadline', self.professionalHeadline, 'skills', self.skills, 'photo_url', self.photo_url))
        else:
            return(
                    "{{ '{}': '{}', '{}': '{}', '{}': '{}', {}: {} }}"
                    .format('public_Id', self.public_Id, 'fullname',
                            self.fullname, 'professionalHeadline', 
                            self.professionalHeadline, 
                            'skills', self.skills))
    
    def update(self, *args, **kwargs):
        """
        Updates the Instatiation with a dictionary
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
