from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.shortcuts import render
import requests

class Dashboard(View):

    @method_decorator(login_required)
    def get(self, request):
        actions = requests.get('http://localhost:8080/actions')
        nbOfActionsToday = requests.get('http://localhost:8080/actions/count?dateTimeRange=2014-07-20-day')
        nbOfActionsThisWeek = requests.get('http://localhost:8080/actions/count?dateTimeRange=2014-29-week')
        nbOfActionsThisMonth = requests.get('http://localhost:8080/actions/count?dateTimeRange=2014-07-month')
        nbOfActionsThisYear = requests.get('http://localhost:8080/actions/count?dateTimeRange=2014-year')

        return render(
            request,
            'dashboard/show.html',
            {
                'actions': actions.json(),
                'nbOfActionsToday': nbOfActionsToday.json(),
                'nbOfActionsThisWeek': nbOfActionsThisWeek.json(),
                'nbOfActionsThisMonth': nbOfActionsThisMonth.json(),
                'nbOfActionsThisYear': nbOfActionsThisYear.json(),
            }
        )
