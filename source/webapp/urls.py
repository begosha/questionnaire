from django.urls import path
from webapp.views.poll_views import (IndexView)

urlpatterns = [
    path('', IndexView.as_view(), name='index')]