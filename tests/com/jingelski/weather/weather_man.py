import unittest
import requests
import yaml
import pathlib
from com.jingelski.weather.weather_man import WeatherMan


class WeatherManTest(unittest.TestCase):

    def setUp(self) -> None:
        project_root_path = pathlib.Path(__file__).resolve().parent.parent.parent.parent.parent #fugly

        config_file_path = project_root_path.joinpath('./config.yml')
        print(config_file_path)

        with open(config_file_path) as config:
            data = yaml.load(config, Loader=yaml.FullLoader)
            self.yahoo_weather_api_endpoint = data['yahoo_weather_api']['endpoint']

    def test_basic_yahoo_connection(self):
        response = requests.get(self.yahoo_weather_api_endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertIsNot(response.json(), '')
        self.assertIsNot('', response.json())
        temperature_json = response.json()['data']['weathers'][0]['observation']['temperature']
        self.assertIsNot(temperature_json, '')
        self.assertIsNot(temperature_json['now'], '')
        self.assertIsNot(temperature_json['high'], '')
        self.assertIsNot(temperature_json['low'], '')

    def test_weather_man(self):
        wm = WeatherMan()
        self.assertIsNotNone(wm.current_temperature)
        self.assertIsNotNone(wm.temperature_low)
        self.assertIsNotNone(wm.temperature_high)


if __name__ == '__main__':
    unittest.main()
