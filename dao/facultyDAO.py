import csv
from config.dbconfig import pg_config
import psycopg2
import psycopg2.extras

class FacultyDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                pg_config['user'],
                                                pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    def getAllFaculty(self):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * FROM faculty"
        cursor.execute(query)

        result = cursor.fetchall()
        cursor.close()

        return result

    def getFacultyById(self, fid):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * from faculty WHERE fid = %s;"
        cursor.execute(query, (fid,))
        result = cursor.fetchone()
        cursor.close()

        return result

    def getFacultyByEmail(self, email):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * from faculty WHERE email = %s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()

        return result

    def getFacultyByPhone(self, phone):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * from faculty WHERE phone = %s;"
        cursor.execute(query, (phone,))
        result = cursor.fetchone()
        cursor.close()

        return result

    def getFacultyByOffice(self, office):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * from faculty WHERE office = %s;"
        cursor.execute(query, (office,))
        result = cursor.fetchone()
        cursor.close()

        return result

    def getFacultyByFirstName(self, firstName):
        cursor = self.conn.cursor()
        query = "select * from faculty where firstName = %s;"
        cursor.execute(query, (firstName,))
        result = []

        for row in cursor:
                result.append(row)

        return result

    def getFacultyByLastName(self, lastName):
        cursor = self.conn.cursor()
        query = "select * from faculty where lastName = %s;"
        cursor.execute(query, (lastName,))
        result = []

        for row in cursor:
                result.append(row)

        return result

    def getFacultyByName(self, firstName, lastName):
        cursor = self.conn.cursor()
        query = "select * from faculty where firstName = %s and lastName = %s;"
        cursor.execute(query, (firstName,lastName,))
        result = []

        for row in cursor:
                result.append(row)

        return result


