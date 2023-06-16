import urllib.request
import urllib.error
import json
import urllib.parse

def get_weather_data(city):
    api_key = "ZQ81IeeKAsMjOybIQMdLN8zgbFNMYT1v"  #
    base_url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city}"

    try:
        response = urllib.request.urlopen(base_url)
        data = json.loads(response.read().decode())
        location_key = data[0]["Key"]
    except urllib.error.URLError as e:
        print("Failed to get your city：", str(e))
        return None

    weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}&details=true"

    try:
        response = urllib.request.urlopen(weather_url)
        weather_data = json.loads(response.read().decode())
        return weather_data
    except urllib.error.URLError as e:
        print("failed to obtain weather information：", str(e))
        return None


city = input("Input Your City Name：")
encoded_city = urllib.parse.quote(city)
weather_data = get_weather_data(encoded_city)

if weather_data:
    print("City：", city)
    print("Weather Situation：", weather_data[0]["WeatherText"])
    print("Temperature：", weather_data[0]["Temperature"]["Metric"]["Value"], "°C")
    print("Humidity：", weather_data[0]["RelativeHumidity"], "%")
else:
    print("Failed for your weather information.")
