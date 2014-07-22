from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.shortcuts import render
from datetime import date
import requests

class Dashboard(View):

    @method_decorator(login_required)
    def get(self, request):
        dateTimeRange = request.GET.get('dateTimeRange', date.today().strftime("%Y-%m-%d-day"))

        nbOfVisits = requests.get('http://localhost:8080/visits/count?dateTimeRange='+dateTimeRange)
        nbOfActions = requests.get('http://localhost:8080/visits/actions/count?dateTimeRange='+dateTimeRange)
        nbOfCountries = requests.get('http://localhost:8080/visits/countries/count?dateTimeRange='+dateTimeRange)

        return render(
            request,
            'dashboard/show.html',
            {
                'nbOfVisits': nbOfVisits.json(),
                'nbOfActions': nbOfActions.json(),
                'nbOfCountries': nbOfCountries.json(),
                'today': date.today(),
            }
        )
