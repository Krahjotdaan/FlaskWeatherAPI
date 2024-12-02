from flask import Flask, request, render_template
from get_weather import *
from check_weather import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        try:
            lat_start = float(request.form["lat_start"])
            lon_start = float(request.form["lat_start"])
            lat_end = float(request.form["lat_end"])
            lon_end = float(request.form["lon_end"])
        except Exception as e:
            pass

        try:
            start_location_key = get_location_key(lat_start, lon_start)
            end_location_key = get_location_key(lat_end, lon_end)
        except Exception as e:
            pass

        start_weather = get_weather_data(start_location_key)
        end_weather = get_weather_data(end_location_key)

        write_weather_data_to_file(lat_start, lon_start, start_weather)
        write_weather_data_to_file(lat_end, lon_end, end_weather)


        return render_template("result.html", 
                               start_point=(lat_start, lon_start), 
                               end_point=(lat_end, lon_end), 
                               start_evaluation=start_weather, 
                               end_evaluation=end_weather)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)