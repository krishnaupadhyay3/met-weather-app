from django.shortcuts import render
from django.views import View
# Create your views here.

class WeatherView(View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': ""})

    def post(self, request, *args, **kwargs):
        pass
