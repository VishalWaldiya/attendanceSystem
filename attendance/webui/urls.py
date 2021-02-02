from django.urls import path
from .views import LamdingPage, MemberListView, index, CreateTransaction

urlpatterns = [
    path('', LamdingPage.as_view()),
    path('sewadaar-list', MemberListView.as_view()),
    path('create-transaction', CreateTransaction.as_view()),
]
