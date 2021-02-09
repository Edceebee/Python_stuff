# first import the mysql connector;
import mysql.connector

# import the error module from mysql connector
from mysql.connector import Error


def connect_insert():
    ''' function to connect and insert a row in a database'''

    # create a connection variable
    conn = None

    try:
        conn = mysql.connector.connect(host='localhost', database='cape_codd', user='Star_boy', password='nonibee'),
        print('connecting to database')
        if conn.is_connected:
            print('Connected to the database')
            db_cursor = conn.cursor()

            # create a variable to contain the sql query to be executed
            sql = "INSERT INTO  human(name, color, gender, Bloodgroup) VALUES (%s, %s, %s, %s)"

            # create a list variable to contain all the values we want to insert into the database
            val = [
                ('Hannah', 'White', 'Female', 'B-'),
                ('1009', 'Michael', 'Brown', 'Male', 'O-'),
                ('1010', 'Sandy', 'Black', 'Male', 'O+'),
                ('1011', 'Green', 'Yellow', 'Male', 'AB'),
                ('1012', 'Richard', 'Black', 'Male', 'B+'),
            ]

        # execute the query using the executemany function
        db_cursor.executemany(sql, val)

        # commit to the database
        conn.commit()

        # print a success message
        print(db_cursor.rowcount, "rows was inserted")

        # close the cursor
        db_cursor.close()

    except Error as e:
        print('Connection failed due to the following :', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Disconnected from database')



# call the function we just created
connect_insert()


# define the connector function
# def connect_fetch():
#     """ function to connect and fetch rows in a database"""
#
#     # create a variable for the connector object
#     conn = None
#
#     try:
#         conn = mysql.connector.Connect(
#             host='localhost',
#             database='cape_codd',
#             user='Star_boy',
#             password='nonibee')
#
#         # what to display once connection is succesfull
#         print("\n Connected to the database")
#
#         # select query
#         sql_select_query = "select * from buyer"
#         # cursor variable
#         cursor = conn.cursor()
#         cursor.execute(sql_select_query)
#         records = cursor.fetchall()
#
#         # print select output
#         print("\n Printing each buyer record")
#         for rows in records:
#             print("Buyer name:", rows[0])
#             print("Department:", rows[0])
#             print("Position:", rows[0])
#             print("Supervisor:", rows[0])
#
#     except Error as e:
#         print('Not connecting due to: ', e)
#     finally:
#         if conn is not None and conn.is_connected():
#             conn.close()
#             print('database shutdown!!, welldone star_boy')
#
#
# connect_fetch()
