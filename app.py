"""
This module implements a Flask web application for comparing weather conditions 
between two geographical locations using the AccuWeather API.
"""

import uuid
import requests
from flask import Flask, request, render_template, flash
from get_weather import *
from check_weather import *


app = Flask(__name__)
app.secret_key = uuid.uuid4().hex


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles GET and POST requests for the main application route.

    GET: Renders the index.html form.
    POST: Processes the form data, retrieves weather information from the AccuWeather API,
          and renders the result.html template with the weather comparison.
    """

    if request.method == "POST":

        try:
            lat_start = float(request.form["lat_start"])
            lon_start = float(request.form["lon_start"])
            lat_end = float(request.form["lat_end"])
            lon_end = float(request.form["lon_end"])

        except ValueError:
            flash("Вводимые параметры должны быть числами с плавающей точкой", 'warning')

        
        start_location_key = None
        end_location_key = None


        try:
            start_location_key = get_location_key(lat_start, lon_start)
            end_location_key = get_location_key(lat_end, lon_end)
        
        except requests.exceptions.HTTPError as e:

            if e.response.status_code == 503:
                flash("API ключ не авторизирован", 'warning')
                return render_template("index.html")
            else:
                flash(f"HTTP Error: {e.response.status_code}")
                return render_template("index.html")

        try:
            start_weather_general = get_weather_data(start_location_key)
            end_weather_general = get_weather_data(end_location_key)
            
        except requests.exceptions.HTTPError as e:

            if e.response.status_code == 503:
                flash("API ключ не авторизирован", 'warning')
                return render_template("index.html")
            else:
                flash(f"HTTP Error: {e.response.status_code}")
                return render_template("index.html")


        start_weather = get_main_params(start_weather_general[0])
        end_weather = get_main_params(end_weather_general[0])

        start_result_str = get_result_str(start_weather)
        end_result_str = get_result_str(end_weather)

        return render_template("result.html", 
                               start_point=', '.join([str(lat_start), str(lon_start)]), 
                               end_point=', '.join([str(lat_end), str(lon_end)]), 
                               start_evaluation=start_result_str,
                               end_evaluation=end_result_str)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
    