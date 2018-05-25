from django.conf.urls import *
from . import views

app_name='calendarManager'

urlpatterns = [
    # urls for websites
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"rawdata", views.RawDataPage.as_view(), name="rawdata"),

    # urls for AJAX requests
    # url(r"renderCalendar", views.renderCalendar, name="todos"),
]
