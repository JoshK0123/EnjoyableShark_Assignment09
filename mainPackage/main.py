# main.py

import random
import pyodbc
from dbUtilitiesPackage.dbUtilities import *

try:
    cursor = DatabaseConnection.connect_to_database()
    
except Exception as e:
    print("Error accessing database")
    print(e)
    exit()

query_string = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID  FROM tProduct"
results = cursor.execute(query_string)
for row in results.fetchall():
    print(row)

