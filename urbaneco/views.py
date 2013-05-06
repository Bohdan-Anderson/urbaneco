from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils import timezone

from urbaneco.models import Event, Person

from django.shortcuts import render_to_response

import datetime

def home(request):
    # View code here...
    return render_to_response('urbaneco/home.html', {"hi" : datetime.datetime.now })

class SpeakerListView(ListView):

    model = Person

    def get_context_data(self, **kwargs):
        context = super(SpeakerListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class SpeakerDetailView(DetailView):

    model = Person

    def get_context_data(self, **kwargs):
        context = super(SpeakerDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class EventListView(ListView):

    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()

        return context


class EventDetailView(DetailView):

    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context