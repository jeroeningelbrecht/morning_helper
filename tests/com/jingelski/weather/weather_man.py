import unittest
import requests
import yaml
import pathlib

class WeatherManTest(unittest.TestCase):

    def setUp(self) -> None:
        project_root_path = pathlib.Path(__file__).parent.parent.parent.parent.parent  # fugly?!
        config_file_path = project_root_path.joinpath('config.yml')

        with open(config_file_path) as config:
            data = yaml.load(config, Loader=yaml.FullLoader)
            self.yahoo_weather_api_endpoint = data['yahoo_weather_api']['endpoint']

    def test_basic_yahoo_connection(self):
        response = requests.get(self.yahoo_weather_api_endpoint)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
