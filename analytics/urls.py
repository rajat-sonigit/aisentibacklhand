

from django.urls import path
from .views import analyze_feedback

urlpatterns = [
    path("analyze/", analyze_feedback, name="analyze_feedback"),
]
