# https://www.youtube.com/watch?v=f1TRDX-TUdg

import mysql.connector as connector
import os

MYSQL_USER = os.environ["MYSQL_USER"]
MYSQL_PASS = os.environ["MYSQL_PASS"]


# Making connection

# con = connector.connect(
#   host="localhost",
#   # port='3306',
#   user=MYSQL_USER,
#   password=MYSQL_PASS,
#   database='mysql'
#   # auth_plugin='mysql_native_password'
# )

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host="localhost",
                                     # port='3306',
                                     user=MYSQL_USER,
                                     MYSQL_PASS=MYSQL_PASS,
                                     database='DBDemoPython')
        cur = self.con.cursor()
        query = 'create table if not exists user(userId int primary key, userName varchar(200), phone varchar(12))'
        cur.execute(query)
        print("Created")

    # Insert
    def insert_user(self, userid, username, phone):
        query = """insert into user(userid, username, phone)
                    values({}, '{}', '{}')""".format(userid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to DB")

    # Fetch all
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("UserId: ", row[0])
            print("UserName: ", row[1])
            print("User Phone: ", row[2])
            print()
            print()

    # Delete user
    def delete_user(self, userid):
        query = "delete from user where userId= {}".format(userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")

    # Update
    def update_user(self, userid, new_name, new_phone):
        query = "update user set userName='{}', phone='{}' where userId = {}".format(new_name, new_phone, userid)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")


helper = DBHelper()
# helper.insert_user(1952, "John", "7035037984")
# helper.insert_user(8352, "Bob", "9034347984")
# helper.insert_user(5452, "Ram", "4098040384")
# helper.insert_user(1932, "Alice", "9434337984")
# helper.insert_user(1342, "Ron", "9034344984")
helper.fetch_all()
helper.delete_user(1342)
helper.fetch_all()
helper.delete_user(1952)
helper.fetch_all()
helper.update_user(8352, "Foo", "9857893487")
helper.fetch_all()

# Some useful queries
# To show databases: show databases;
# To check which database is in used: select database() from dual;
# To switch database: use NewDatabase;
# To show list of databases: show tables;
# To create database: create database NewDatabase;
# To create table: create table if not exists Customer(customerId int primary key, customerName varchar(200), phone varchar(12))

