# -*- coding: utf-8 -*-

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.shortcuts import render
from datetime import date
from gonalytics import settings
import jsondatetime as json
import requests
import json

class Dashboard(View):

    @method_decorator(login_required)
    def get(self, request):
        dateTimeRange = request.GET.get('dateTimeRange', date.today().strftime("%Y-%m-%d-day"))

        visitsLive = requests.get(settings.GONALYTICS_TRACKER_URL+'/visits/live?limit=5&outputFormat=json')
        visitsGroupedByFirstAction = requests.get(settings.GONALYTICS_TRACKER_URL+'/visits/group/first-action/'+dateTimeRange+'?outputFormat=json')
        visitsGroupedByCountryCode = requests.get(settings.GONALYTICS_TRACKER_URL+'/visits/group/country-code/'+dateTimeRange+'?outputFormat=json')

        nbOfVisits = requests.get(settings.GONALYTICS_TRACKER_URL+'/visits/count?dateTimeRange='+dateTimeRange+'&outputFormat=json')
        nbOfActions = requests.get(settings.GONALYTICS_TRACKER_URL+'/visits/actions/count?dateTimeRange='+dateTimeRange+'&outputFormat=json')
        nbOfCountries = requests.get(settings.GONALYTICS_TRACKER_URL+'/visits/countries/count?dateTimeRange='+dateTimeRange+'&outputFormat=json')
        averageDuration = requests.get(settings.GONALYTICS_TRACKER_URL+'/visits/average-duration?dateTimeRange='+dateTimeRange+'&outputFormat=json')

        return render(
            request,
            'dashboard/show.html',
            {
                'visitsGroupedByFirstAction': json.loads(json.dumps(visitsGroupedByFirstAction.text, default=dthandler)),
                'visitsGroupedByCountryCode': json.loads(json.dumps(visitsGroupedByCountryCode.text, default=dthandler)),
                'visitsLive': visitsLive.json(),
                'nbOfVisits': nbOfVisits.json(),
                'nbOfActions': nbOfActions.json(),
                'nbOfCountries': nbOfCountries.json(),
                'today': date.today(),
                'averageDuration': averageDuration.json() / (6000000000.00),
            }
        )

dthandler = lambda obj: (
    obj.isoformat()
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date)
    else None)
