from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name="events/home"),
    path('events', views.all_events, name="list-events"),
    path('add_event', views.add_event, name='add-event'),
    path('search_event', views.search_event, name='search-event'),
    #path('delete-event<int:mobile_no>', views.delete_event, name='delete-event'),
    path('delete_event/<int:pk>', views.delete_event, name='delete_event'),
    path('update_event/<int:pk>', views.update_event, name='update_event'),
    path('event_text', views.event_text, name='event_text'),
    path('event_csv', views.event_csv, name='event_csv'),
    path('event_pdf', views.event_pdf, name='event_pdf'),

]
