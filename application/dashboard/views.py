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

        nbOfActionsByCountryResponse = requests.get(settings.GONALYTICS_TRACKER_URL+'/sites/1/nb-of-actions-by-country?=timestamp='+dateTimeRange)
        nbOfActionsByBrowserResponse = requests.get(settings.GONALYTICS_TRACKER_URL+'/sites/1/nb-of-actions-by-browser?=timestamp='+dateTimeRange)

        nbOfVisitsByCountryResponse = requests.get(settings.GONALYTICS_TRACKER_URL+'/sites/1/nb-of-visits-by-country?=timestamp='+dateTimeRange)
        nbOfVisitsByBrowserResponse = requests.get(settings.GONALYTICS_TRACKER_URL+'/sites/1/nb-of-visits-by-browser?=timestamp='+dateTimeRange)

        nbOfActionsByCountry = nbOfActionsByCountryResponse.json()
        nbOfActionsByBrowser = nbOfActionsByBrowserResponse.json()
        nbOfVisitsByCountry = nbOfVisitsByCountryResponse.json()
        nbOfVisitsByBrowser = nbOfVisitsByBrowserResponse.json()

        nbOfActions = 0
        nbOfVisits = 0
        visitsGroupedByCountryCode = {}

        for nbOfActionsForBrowser in nbOfActionsByBrowser:
            nbOfActions += nbOfActionsForBrowser['count']

        for nbOfVisitsForBrowser in nbOfVisitsByBrowser:
            nbOfVisits += nbOfVisitsForBrowser['count']

        for nbOfActionsForCountry in nbOfActionsByCountry:
            visitsGroupedByCountryCode[nbOfActionsForCountry['locationCountryCode']] = nbOfActionsForCountry['count']

        return render(
            request,
            'dashboard/show.html',
            {
                'nbOfActions': nbOfActions,
                'nbOfVisits': nbOfVisits,
                'nbOfCountries': len(nbOfVisitsByCountry),
                'nbOfActionsByCountry': nbOfActionsByCountry,
                'nbOfActionsByBrowser': nbOfActionsByBrowser,
                'nbOfVisitsByCountry': nbOfVisitsByCountry,
                'nbOfVisitsByBrowser': nbOfVisitsByBrowser,
                'visitsGroupedByCountryCode': json.dumps(visitsGroupedByCountryCode, default=dthandler),
                # 'distributionByTime': json.loads(json.dumps(visitsGroupedByCountryCode, default=dthandler)),
                # 'visitsLive': visitsLive.json(),
                'today': date.today(),
                # 'averageDuration': averageDuration.json() / (6000000000.00),
            }
        )

dthandler = lambda obj: (
    obj.isoformat()
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date)
    else None)
