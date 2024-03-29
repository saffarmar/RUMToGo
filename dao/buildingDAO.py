import csv
from config.dbconfig import pg_config
import psycopg2
import psycopg2.extras

class BuildingDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                pg_config['user'],
                                                pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    def getAllBuilding(self):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * FROM buildings"
        cursor.execute(query)

        result = cursor.fetchall()
        cursor.close()

        return result

    def getBuildingById(self, bid):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT * from buildings WHERE bid = %s;"
        cursor.execute(query, (bid,))
        result = cursor.fetchone()
        cursor.close()

        return result

    def getBuildingByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from buildings where name = %s;"
        cursor.execute(query, (name,))
        result = []

        for row in cursor:
                result.append(row)

        return result

