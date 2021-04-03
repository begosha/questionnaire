from django.urls import path
from webapp.views.poll_views import (IndexView, PollAddView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', PollAddView.as_view(), name='poll-add'),
]