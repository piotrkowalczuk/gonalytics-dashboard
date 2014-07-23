from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.shortcuts import render
from datetime import date
import jsondatetime as json
import requests
import json

class Dashboard(View):

    @method_decorator(login_required)
    def get(self, request):
        dateTimeRange = request.GET.get('dateTimeRange', date.today().strftime("%Y-%m-%d-day"))

        visitsLive = requests.get('http://localhost:8080/visits/live')
        visits = requests.get('http://localhost:8080/visits?dateTimeRange='+dateTimeRange)

        nbOfVisits = requests.get('http://localhost:8080/visits/count?dateTimeRange='+dateTimeRange)
        nbOfActions = requests.get('http://localhost:8080/visits/actions/count?dateTimeRange='+dateTimeRange)
        nbOfCountries = requests.get('http://localhost:8080/visits/countries/count?dateTimeRange='+dateTimeRange)

        return render(
            request,
            'dashboard/show.html',
            {
                'visits': json.loads(json.dumps(visits.text, default=dthandler)),
                'visitsLive': visitsLive.json(),
                'nbOfVisits': nbOfVisits.json(),
                'nbOfActions': nbOfActions.json(),
                'nbOfCountries': nbOfCountries.json(),
                'today': date.today(),
            }
        )
dthandler = lambda obj: (
    obj.isoformat()
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date)
    else None)
