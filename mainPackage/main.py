# main.py

import random
import pyodbc
from dbUtilitiesPackage.dbUtilities import *

if __name__ == "__main__":
    """
    This package attempts to connect to the DB and uses queries and its data to make a sentence of it
    """
    try:
        cursor = DatabaseConnection.connect_to_database()
    
    except Exception as e:
        print("Error accessing database")
        print(e)
        exit()
        
    emptyListForData = []
    query_string = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID  FROM tProduct"
    results = cursor.execute(query_string)
    for row in results.fetchall(): 
        emptyListForData.append(row)
    random_row_from_list = random.choice(emptyListForData)
    
    productID = random_row_from_list[0]
    description = random_row_from_list[2]
    manufacturerID = random_row_from_list[3]
    brandID = random_row_from_list[4]
    
    query_string_manufacturer = "SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = " + str(manufacturerID)
    Manufacturer = cursor.execute(query_string)
    for row in results.fetchall(): 
        Manufacturer = row

    query_string_brand = "SELECT Brand FROM tBrand WHERE BrandID = " + str(brandID)
    Brand = cursor.execute(query_string)
    for row in results.fetchall(): 
        Brand = row

