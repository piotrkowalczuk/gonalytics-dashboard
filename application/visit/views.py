from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.shortcuts import render
import requests

class VisitList(View):

    @method_decorator(login_required)
    def get(self, request):
        visits = requests.get('http://localhost:8080/visits')

        return render(
            request,
            'visit/list.html',
            {
                'visits': visits.json(),
            }
        )
