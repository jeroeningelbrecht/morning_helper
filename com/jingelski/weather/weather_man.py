import requests
import pathlib
import yaml
from com.jingelski.util.util import round_half_up


class WeatherMan:

    def __init__(self):
        project_root_path = pathlib.Path(__file__).parent.parent.parent.parent  # fugly?!
        config_file_path = project_root_path.joinpath('config.yml')

        with open(config_file_path) as config:
            data = yaml.load(config, Loader=yaml.FullLoader)
            self.yahoo_weather_api_endpoint = data['yahoo_weather_api']['endpoint']

        self.json_data = requests.get(self.yahoo_weather_api_endpoint).json()

        # calculate the current temperature, the predicted max and predicted min
        self._calc_temperatures()

        self.observation_json = self.json_data['data']['weathers'][0]['observation']
        self.precipitationProbability = self.observation_json['precipitationProbability']
        self.current_wind_speed = round_half_up(float(self.observation_json['windSpeed']) * 1.609344, 1)

    def update(self) -> None:
        self.json_data = requests.get(self.yahoo_weather_api_endpoint)
        self.__calc_temperatures()

    def _calc_temperatures(self):
        self.current_temperature = round_half_up((float(self.json_data['data']['weathers'][0]['observation']['temperature']['now']) - 32)/1.8, 1)
        self.temperature_high = round_half_up((float(self.json_data['data']['weathers'][0]['observation']['temperature']['high']) - 32)/1.8, 1)
        self.temperature_low = round_half_up((float(self.json_data['data']['weathers'][0]['observation']['temperature']['low']) - 32)/1.8, 1)
