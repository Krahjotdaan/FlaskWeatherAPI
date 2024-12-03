from flask import Flask, request, render_template
from get_weather import *
from check_weather import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        lat_start = float(request.form["lat_start"])
        lon_start = float(request.form["lon_start"])
        lat_end = float(request.form["lat_end"])
        lon_end = float(request.form["lon_end"])

        start_location_key = get_location_key(lat_start, lon_start)
        end_location_key = get_location_key(lat_end, lon_end)

        start_weather_general = get_weather_data(start_location_key)
        end_weather_general = get_weather_data(end_location_key)

        write_weather_data_to_file(lat_start, lon_start, start_weather_general)
        write_weather_data_to_file(lat_end, lon_end, end_weather_general)

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