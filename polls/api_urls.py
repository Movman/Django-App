# API urls here



from django.urls import path

from . import api_views


urlpatterns = [
    path('', api_views.pollsList, name="polls-list"),
    path('<int:pk>/', api_views.pollsDetail, name="polls-detail"),
]