from django.urls import path
from .views import LamdingPage

urlpatterns = [
    # path('', index),
    path('', LamdingPage.as_view()),
]
