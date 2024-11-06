#dbUtilities.py

# Name: Joshua Klingelhafer, Lucas Ransick, Ryan Dew
# email: klingejh@mail.uc.edu, ransiclg@mail.uc.edu, dewrm@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:  11/7
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Connect to a database and create SQL queries to learn about grocery items from a database.
# Brief Description of what this module does: This module connects us to the SQL database.
# Citations: Stack Overflow
# Anything else that's relevant:

import pyodbc
class DatabaseConnection(object):
    """
    Establishes a connection to a database
    """
    def __init__(self, conn):
        """
        Constructor
        @param conn Connection: Connection object to connect to database
        """
        self.__conn = conn
        
    def connect_to_database():
        """
        Connect to the database
        @return Connection Object: The open connection, or None on error
        """
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                          'Database=GroceryStoreSimulator;'
                          'uid=IS4010Login;'
                          'pwd=P@ssword2;')
        except:
            conn = None
        
        return conn
        
    def __str__(self):
        """
        @return String: A human-readable basic representation of the current object. 
        """
        return "model: " + self.__conn

    def __repr__(self):
        """
        @return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"Connection('{self.__conn}')"
        
