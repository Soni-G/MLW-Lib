"""
This module contains MLW HTTPClient class and its related functions
"""

import getpass
import requests
from requests.auth import HTTPBasicAuth


class HTTPClient():
    """
    HTTPClient class, contains HTTP configuration methods for MLW application.

    """
    def __init__(self, c8y_base_url):
        """ 
        init method of HTTPClient class
        
        :param c8y_base_url: url of MLW tenant
        :type c8y_base_url: String
        """
        self.c8y_base_url = c8y_base_url
        self.__auth = HTTPBasicAuth(input('Enter username:  '), getpass.getpass(prompt='Enter password: '))
        self.request_session = requests.session()
        self.request_session.auth = self.__auth
    
    def configure(self, c8y_base_url):
        """ 
        configure method of HTTPClient class
        
        :param c8y_base_url: url of MLW tenant
        :type c8y_base_url: String
        """
        self.c8y_base_url = c8y_base_url
        self.__auth = HTTPBasicAuth(input('Enter username:  '), getpass.getpass(prompt='Enter password: '))
        self.request_session = requests.session()
        self.request_session.auth = self.__auth
