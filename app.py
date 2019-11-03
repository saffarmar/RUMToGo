from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
from dao.buildingDAO import BuildingDao
from dao.facultyDAO import FacultyDao
from dao.floormapDAO import FloormapDao
from dao.locationDAO import LocationDao
from dao.parkingDAO import ParkingDao
from functools import wraps
#from passlib.hash import sha256_crypt

app = Flask(__name__)

app.config['DEBUG'] = True # Debug Mode. Server is reloaded on any code change
                           # and provides detailed error messages.
app.config['SECRET_KEY'] = 'RUMTOGo'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

@app.route('/maps')
def faculty():
    return render_template('maps.html')

if __name__ == '__main__':
    app.run()
