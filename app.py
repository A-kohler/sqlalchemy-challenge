import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func ,inspect
from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite")


Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station


inspector = inspect(engine)
inspector.get_table_names()


app = Flask(__name__)


@app.route("/")
def home():
    return("/api/v1.0/precipitation<br/>"
    "/api/v1.0/stations<br/>"
    "/api/v1.0/tobs<br/>"
    "/api/v1.0/2017-01-01<br/>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    results1 = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>="2016-08-23").all()
    first_dict = list(np.ravel(results1))

first_dict = []
       for temps in results1:
         temps_dict = {}
         temps_dict["date"] = Measurement.date
         temps_dict["tobs"] = Measurement.tobs
         first_dict.append(temps_dict)



  `/api/v1.0/stations`


@app.route("/api/v1.0/stations")
def stations():
    results2 = session.query(Station.station, Station.name).all()

    sec_dict = list(np.ravel(results2))
    sec_dict = []
    for sta in results2:
    station_dict = {}
    station_dict["station"] = Station.station
    station_dict["name"] = Station.name
    sec_dict.append(station_dict)


    return jsonify(sec_dict)


   `/api/v1.0/tobs`

@app.route("/api/v1.0/tobs")
def tobs():
    results3 = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.date>="2016-08-23").\
            filter(Measurement.date<="2017-08-23").all()

            
    temp_dict = list(np.ravel(results3))

     third_dict = []
     for temps in results3:
         temp_dict = {}
         temp_dict["date"] = Measurement.date
         temp_dict["tobs"] = Measurement.tobs
         third_dict.append(temp_dict)

    return jsonify(temp_dict)


  `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`


@app.route("/api/v1.0/<date>")

def start1(date):

    results4 = session.query((Measurement.date, func.avg(Measurement.tobs), func.max(Measurement.tobs), func.min(Measurement.tobs)).\
            filter(Measurement.date)>=date).all()
   

    five_dict = []
    for s in results4:
        
         start_dict = {}
         start_dict["Date"] = float(s[0])
         start_dict["Avg"] = float(s[1])
         start_dict["Min"] = float(s[2])
         start_dict["Max"] = float(s[3])
         five_dict.append(start_dict)

        start_dict = {}
        start_dict["Date"] = s.Date
        start_dict["Avg"] = s.func.avg(Measurement.tobs)
        start_dict["Min"] = s.func.min(Measurement.tobs)
        start_dict["Max"] = s.func.max(Measurement.tobs)
        five_dict.append(start_dict)

    return jsonify(five_dict)
    return jsonify(temp_dates)

    
if __name__ == '__main__':
    app.run(debug=True)
