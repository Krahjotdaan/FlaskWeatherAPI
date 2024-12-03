
def get_main_params(data: dict):
    main_params = {}

    main_params["temp"] = data["Temperature"]["Metric"]["Value"]
    main_params["feel_temp"] = data["RealFeelTemperature"]["Metric"]["Value"]
    main_params["weather_text"] = data["WeatherText"]
    main_params["precipitation"] = data["HasPrecipitation"]
    main_params["humidity"] = data["RelativeHumidity"]
    main_params["wind_speed"] = round(data["Wind"]["Speed"]["Metric"]["Value"] * 1000 / 3600, 1)
    main_params["direction"] = data["Wind"]["Direction"]["English"]
    main_params["pressure"] = data["Pressure"]["Metric"]["Value"]

    return main_params


def get_result_str(main_params: dict):
    result_str = ""

    result_str += f'Температура: {main_params["temp"]}C \n'
    result_str += f'Ощущается как: {main_params["feel_temp"]}C \n'
    result_str += f'Погода: {main_params["weather_text"]} \n'
    result_str += f'Осадки: {main_params["precipitation"]} \n'
    result_str += f'Относительная влажность: {main_params["humidity"]}% \n'
    result_str += f'Скорость ветра: {main_params["wind_speed"]} м/c \n'
    result_str += f'Направление ветра: {main_params["direction"]} \n'
    result_str += f'Давление: {main_params["pressure"]} гПа \n'

    is_bad_weather = check_bad_weather(main_params)
    if is_bad_weather:
        result_str += f"Погода неблагоприятная \n"
    else:
        result_str += f"Погода хорошая \n\n"

    return result_str


def check_bad_weather(main_params):

    if main_params["precipitation"]:
        return True
    if main_params["feel_temp"] < -10 or main_params["feel_temp"] > 30:
        return True
    if main_params["wind_speed"] > 10:
        return True
    if main_params["pressure"] < 1024 * 0.7 or main_params["pressure"] > 1024 * 2.5:
        return True
    
    return False
