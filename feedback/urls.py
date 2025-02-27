from django.urls import path
from .views import submit_feedback, list_feedback

urlpatterns = [
    path('submit/', submit_feedback, name='submit_feedback'),
    path('list/', list_feedback, name='list_feedback'),
]
