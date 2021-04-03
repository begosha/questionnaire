from django.urls import path
from webapp.views.poll_views import (IndexView, PollAddView, PollView, PollUpdateView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', PollView.as_view(), name='poll'),
    path('add/', PollAddView.as_view(), name='poll-add'),
    path('<int:pk>/update/poll', PollUpdateView.as_view(), name='poll-update'),
]