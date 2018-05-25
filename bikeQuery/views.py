from django.shortcuts import render
from django.views.generic.base import TemplateView

from .src.poznanStations import PoznanStations

# Create your views here.


class HomePage(TemplateView):

    template_name = "bikeQuery/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        responseUrl = "http://www.poznan.pl/mim/plan/map_service.html?mtype=pub_transport&co=stacje_rowerowe"
        context['stationData'] = PoznanStations(responseUrl).getStationData()

        return context


class RawDataPage(TemplateView):

    template_name = "bikeQuery/rawdata.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        responseUrl = "http://www.poznan.pl/mim/plan/map_service.html?mtype=pub_transport&co=stacje_rowerowe"
        context['stationData'] = PoznanStations(responseUrl).getStationData()

        return context
