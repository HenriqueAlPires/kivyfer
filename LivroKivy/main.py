from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.uix.listview import ListItemButton
import json



class CurrentWeather(BoxLayout):
    location = ListProperty(['São Paulo', 'BR'])
    conditions = StringProperty()
    temp = NumericProperty()
    temp_min = NumericProperty()
    temp_max = NumericProperty()

    def update_weather(self):
        weather_template = "http://api.openweathermap.org/data/2.5/" + "weather?q={},{}&lang=pt&units=metric" + "&APPID=fdd52208691033461a1899bdadfe47e8"

        weather_url = weather_template.format(*self.location)
        request = UrlRequest(weather_url, self.weather_retrieved)

    def weather_retrieved(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        self.conditions = data['weather'][0]['description'].upper()
        self.temp = data['main']['temp']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']

    def get_forecast(self):
        forecast_template = "http://api.openweathermap.org/data/2.5/" + "forecast?q={},{}&lang=pt&units=metric&type=like&mode=json" + "&APPID=fdd52208691033461a1899bdadfe47e8"
        forecast_url = forecast_template.format(*self.location)
        request = UrlRequest(forecast_url, self.forecast_retrieve)

    def forecast_retrieve(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        self.conditions = data['list'][7]['weather'][0]['description']
        self.temp = data['list'][7]['main']['temp']
        self.temp_max = data['list'][7]['main']['temp_max']
        self.temp_min = data['list'][7]['main']['temp_min']


class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()

    def show_current_weather(self, location = None):
    #Limpa a tela de widgets, adiciona o widget
        self.clear_widgets()
        if self.current_weather is None:
            self.current_weather = CurrentWeather()

        if location is not None:
            self.current_weather.location = location

        self.current_weather.update_weather()
        self.add_widget(self.current_weather)

    def show_add_location_form(self):
        self.clear_widgets()
        self.add_widget(AddLocationForm())


class LocationButton(ListItemButton):
    #Codigo em conjunto com .kv para mudar a cor dos botôes
    background_color = [1,1,1,1]
    location = ListProperty()


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()


    def args_converter(self, index, data_item):
        city, country = data_item
        return  {'location':(city, country)}

    def search_location(self):
    #API utilizada para pesquisar locais, com .format sendo o texto do "TextInput"
    #Também pega os dados da URL formatados em .json e coloca na variavel "request"
        search_template = "http://api.openweathermap.org/data/2.5/" + "find?q={}&lang=pt&type=like&mode=json" + "&APPID=fdd52208691033461a1899bdadfe47e8"
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
    #Função chamada pela search_location para formatar os dados pedidos para uma lista
    #chamada cities, então adiciona os dados de cities ao adapter e atualiza
        data = json.loads(data.encode()) if not isinstance(data, dict) else data
        cities = [(d['name'], d['sys']['country']) for d in data['list']]
        self.search_results.item_strings = cities
        self.search_results.adapter.data.clear()
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()

class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()
