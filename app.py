from flask import Flask, request
import sqlite3
import requests
from tqdm import tqdm
import json 
import numpy as np
import pandas as pd

app = Flask(__name__) 


#### Functions ####

def make_connection():
    connection = sqlite3.connect('austin_bikeshare.db')
    return connection

conn = make_connection()

def get_station_id(station_id, conn):
    query = f"""SELECT * FROM stations WHERE station_id = {station_id}"""
    result = pd.read_sql_query(query, conn)
    return result 

def get_all_stations(conn):
    query = f"""SELECT * FROM stations"""
    result = pd.read_sql_query(query, conn)
    return result

def get_trip_id(trip_id, conn):
    query = f"""SELECT * FROM trips WHERE id = {trip_id}"""
    result = pd.read_sql_query(query, conn)
    return result
    
def get_all_trips(conn):
    query = f"""SELECT * FROM trips"""
    result = pd.read_sql_query(query, conn)
    return result

def insert_into_stations(data, conn):
    query = f"""INSERT INTO stations values {data}"""
    try:
        conn.execute(query)
    except:
        return 'Error'
    conn.commit()
    return 'OK'

def insert_into_trips(data, conn):
    query = f"""INSERT INTO trips values {data}"""
    try:
        conn.execute(query)
    except:
        return 'Error'
    conn.commit()
    return 'OK'


#### Static Endpoints ####

@app.route('/')
@app.route('/homepage')
def home():
    return 'Hello World'

@app.route('/stations/')
def route_all_stations():
    conn = make_connection()
    stations = get_all_stations(conn)
    return stations.to_json()
    
def get_all_stations(conn):
    query = f"""SELECT * FROM stations"""
    result = pd.read_sql_query(query, conn)
    return result

@app.route('/trips/')
def route_all_trips():
    conn = make_connection()
    trips = get_all_trips(conn)
    return trips.to_json()
    
def get_all_trips(conn):
    query = f"""SELECT * FROM trips"""
    result = pd.read_sql_query(query, conn)
    return result


#### Dynamic Endpoints ####

@app.route('/stations/<station_id>')
def route_stations_id(station_id):
    conn = make_connection()
    station = get_station_id(station_id, conn)
    return station.to_json()

@app.route('/trips/<trip_id>')
def route_trips_id(trip_id):
    conn = make_connection()
    trip = get_trip_id(trip_id, conn)
    return trip.to_json()


#### Handling Json Data ####

@app.route('/json', methods=['POST']) 
def json_example():
    
    req = request.get_json(force=True) # Parse the incoming json data as Dictionary
    
    name = req['name']
    age = req['age']
    address = req['address']
    
    return (f'''Hello {name}, your age is {age}, and your address in {address}
            ''')


@app.route('/stations/add', methods=['POST']) 
def route_add_station():
    # parse and transform incoming data into a tuple as we need 
    data = pd.Series(eval(request.get_json(force=True)))
    data = tuple(data.fillna('').values)
    
    conn = make_connection()
    result = insert_into_stations(data, conn)
    return result

@app.route('/trips/add', methods=['POST']) 
def route_add_trip():
    # parse and transform incoming data into a tuple as we need 
    data = pd.Series(eval(request.get_json(force=True)))
    data = tuple(data.fillna('').values)
    
    conn = make_connection()
    result = insert_into_trips(data, conn)
    return result

#### Dynamic Endpoints ####
# example of analytical static endpoint 
@app.route('/trips/average_duration', methods=['GET']) 
def calculate_average_duration():
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(duration_minutes) FROM trips")
    avg_duration = cursor.fetchone()[0]

    response_data = json.dumps({"average_duration": avg_duration})
    
    return response_data

@app.route('/trips/average_duration/<bike_id>', methods=['GET']) 
def calculate_average_duration_by_id(bike_id):
    conn = sqlite3.connect('austin_bikeshare.db')

   # Query to calculate the average duration for the specified bike_id
    query = f"SELECT AVG(duration_minutes) as average_duration FROM trips WHERE bikeid = {bike_id}"
    df = pd.read_sql_query(query, conn)

    # Convert the DataFrame to JSON
    response_data = df.to_json(orient='records')
    # response = Response(response_data, content_type='application/json')

    return response_data

#### Dynamic Endpoints ####


@app.route('/trips/aggregation', methods=['POST'])
def aggregate_bike_rent_activities():
    # Get the input as dictionary
    input_data = request.get_json()

    # Extract the specified period from the input data
    specified_date = input_data['period']  # e.g., "2015-08"

    # Subset the data with query using the specified period
    conn = make_connection()
    query = f"SELECT * FROM trips WHERE start_time LIKE '{specified_date}%'"
    selected_data = pd.read_sql_query(query, conn)

    # Perform aggregation on the selected data
    result = selected_data.groupby('start_station_id').agg({
        'bikeid': 'count', 
        'duration_minutes': 'mean'
    }).reset_index()

    # Convert the result to JSON and return it
    return result.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True, port=5000)