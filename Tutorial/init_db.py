# Add the necessary imports
import mysql.connector as mysql
import os
import datetime
from dotenv import load_dotenv


load_dotenv()


# Read Database connection variables
db_host = "localhost"
db_user = "root"
db_pass = os.environ['MYSQL_ROOT_PASSWORD']


# Connect to the db and create a cursor object
db = mysql.connect(user=db_user, password=db_pass, host=db_host)
cursor = db.cursor()

cursor.execute("CREATE DATABASE if not exists TechAssignment5")
cursor.execute("USE TechAssignment5")

cursor.execute("drop table if exists Roster;")
try:
   cursor.execute("""
   CREATE TABLE Roster(
       id          integer  AUTO_INCREMENT PRIMARY KEY,
       name        VARCHAR(50) NOT NULL,
       role VARCHAR(50) NOT NULL,    
       email       VARCHAR(50) NOT NULL,
       created_at  TIMESTAMP
   );
 """)
except RuntimeError as err:
   print("runtime error: {0}".format(err))

query = "insert into Roster(name, role, email, created_at) values (%s, %s, %s, %s)"
values = [
 ('Ramsin Khoshabeh', 'Professor', 'ramsin@artofproduct.com' , datetime.datetime.now()),
 ('Rick Gessner', 'Professor', 'rick@artofproduct.com', datetime.datetime.now()),
 ('Girish Krishnan','Teaching Assistant', 'girish@artofproduct.com', datetime.datetime.now()),
 ('Emin Kirimlioglu','Teaching Assistant', 'emin@artofproduct.com', datetime.datetime.now()),
 ('Dominic Orlando','Teaching Assistant', 'dominic@artofproduct.com', datetime.datetime.now()),
 ('James Chen','Teaching Assistant', 'james@artofproduct.com', datetime.datetime.now()),
 ('Charles Lee','Teaching Assistant', 'charles@artofproduct.com', datetime.datetime.now()),
]
cursor.executemany(query, values)
db.commit()
