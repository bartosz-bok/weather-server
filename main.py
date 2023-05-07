from flask import Flask, render_template, request
import datetime as dt
import requests


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()

Flask_App = Flask(__name__)  # Creating our Flask Instance


@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')


@Flask_App.route('/check_weather/', methods=['POST'])
def check_weather():
    """Route where we send calculator form input"""

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= "
    city_input = request.form['city']

    try:
        CITY = city_input

        url = BASE_URL + "&q=" + CITY + "&appid=" + API_KEY

        response = requests.get(url).json()
        temp_kelvin = response['main']['temp']
        temp_celsius = round(kelvin_to_celsius(temp_kelvin), 3)

        result = temp_celsius

        return render_template(
            'index.html',
            city=city_input,
            result=result,
            is_success=True
        )

    except ValueError:
        return render_template(
            'index.html',
            result="Bad Input",
            is_success=False,
            error="Blad"
        )


if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()
