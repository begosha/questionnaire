from django.urls import path
from .views import (IndexView, PollAddView, PollView, PollUpdateView, PollDeleteView, ChoiceCreateView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', PollView.as_view(), name='poll'),
    path('add/', PollAddView.as_view(), name='poll-add'),
    path('<int:pk>/update/poll', PollUpdateView.as_view(), name='poll-update'),
    path('<int:pk>/delete', PollDeleteView.as_view(), name='poll-delete'),
    path('<int:pk>/add/', ChoiceCreateView.as_view(), name='choice-add'),
]