from django.urls import path
from .views import LandingPage, MemberListView, index, CreateTransaction

urlpatterns = [
    path('', LandingPage.as_view(), name="home"),
    path('sewadaar-list', MemberListView.as_view()),
    path('create-transaction', CreateTransaction.as_view()),
]
