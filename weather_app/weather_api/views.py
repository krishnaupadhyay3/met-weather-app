from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
import json, requests
# Create your views here.

Weather_Api = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}"
header = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9"}
class WeatherView(View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        
        location = data.get("location").split(",")
        lat  = location[0]
        long = location[1]
        url = Weather_Api.format(lat, long)
        response = requests.get(url, headers=header)
        data = response.json()
        coordinate =  data["geometry"]["coordinates"]
        time_series = data["properties"]["timeseries"][0]["data"]
        data = {
            "coordinate": str(coordinate[0])+" ,"+ str(coordinate[1]),
            "temp": str(time_series["instant"]["details"]['air_temperature'])+"	°C",
            "pressure": str(time_series["instant"]["details"]['air_pressure_at_sea_level'])+" hPa",
            "humidity": str(time_series["instant"]["details"]['relative_humidity'])+" %",
        }

        return JsonResponse(data)
