import mysql.connector
from mysql.connector import Error


def connect():
    print('Lets try and connect to the database!')
    try:
        print('Trying to connect to database')
        conn = mysql.connector.connect(host='localhost',
                                       database='Child_Companion',
                                       user='up750148@yazinstance',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()
