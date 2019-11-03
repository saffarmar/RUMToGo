import csv
from config.dbconfig import pg_config
import psycopg2
import psycopg2.extras

class LocationDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                pg_config['user'],
                                                pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    def getAllLocation(self):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * FROM location"
        cursor.execute(query)

        result = cursor.fetchall()
        cursor.close()

        return result

    def getLocationById(self, lid):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * from location WHERE lid = %s;"
        cursor.execute(query, (lid,))
        result = cursor.fetchone()
        cursor.close()

        return result

