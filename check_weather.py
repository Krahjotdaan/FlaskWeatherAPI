def get_main_params(data):
    main_params = {}

    main_params["temp"] = data["Temperature"]["Metric"]["Value"]
    main_params["feel_temp"] = data["RealFeelTemperature"]["Metric"]["Value"]
    main_params["weather_text"] = data["WeatherText"]
    main_params["precipitation"] = data["HasPrecipitation"]
    main_params["humidity"] = data["RelativeHumidity"]
    main_params["wind_speed"] = data["Wind"]["Speed"]["Metric"]["Value"] * 1000 / 3600
    main_params["direction"] = data["Wind"]["Direction"]["English"]
    main_params["pressure"] = data["Pressure"]["Metric"]["Value"]

    return main_params


def check_bad_weather(data):
    main_params = get_main_params(data)

    if main_params["precipitation"]:
        return True
    if main_params["feel_temp"] < -10 or main_params["feel_temp"] > 30:
        return True
    if main_params["wind_speed"] > 40:
        return True
    if main_params["pressure"] < 1024 * 0.7 or main_params["pressure"] > 1024 * 2.5:
        return True
    
    return False
