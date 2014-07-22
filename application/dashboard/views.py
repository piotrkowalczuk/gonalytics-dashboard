from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.shortcuts import render
import requests

class Dashboard(View):

    @method_decorator(login_required)
    def get(self, request):
        visits = requests.get('http://localhost:8080/visits')
        nbOfVisistsToday = requests.get('http://localhost:8080/visits/count?dateTimeRange=2014-07-21-day')
        nbOfVisistsThisWeek = requests.get('http://localhost:8080/visits/count?dateTimeRange=2014-30-week')
        nbOfVisistsThisMonth = requests.get('http://localhost:8080/visits/count?dateTimeRange=2014-07-month')
        nbOfVisistsThisYear = requests.get('http://localhost:8080/visits/count?dateTimeRange=2014-year')

        return render(
            request,
            'dashboard/show.html',
            {
                'visits': visits.json(),
                'nbOfVisitsToday': nbOfVisistsToday.json(),
                'nbOfVisitsThisWeek': nbOfVisistsThisWeek.json(),
                'nbOfVisitsThisMonth': nbOfVisistsThisMonth.json(),
                'nbOfVisitsThisYear': nbOfVisistsThisYear.json(),
            }
        )
