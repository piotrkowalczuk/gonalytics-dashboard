from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.shortcuts import render
import requests

class Dashboard(View):

    @method_decorator(login_required)
    def get(self, request):
        r = requests.get('http://localhost:8080/actions')

        return render(
            request,
            'dashboard/show.html',
            {
                'actions': r.json()
            }
        )
