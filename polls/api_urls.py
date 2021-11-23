# API urls here

from django.urls import path

from . import api_views


urlpatterns = [
    path('', api_views.PollsList.as_view(), name="polls-list"),
    path('<int:pk>/', api_views.PollsDetail.as_view(), name="polls-detail"),
    path('<int:pk>/vote/', api_views.voteView, name="polls-votes"),
]