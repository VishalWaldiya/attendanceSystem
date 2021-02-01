from django.urls import path
from .views import LamdingPage, MemberListListView, index, CreateTransaction

urlpatterns = [
    path('', LamdingPage.as_view()),
    path('sewadaar-list', MemberListListView.as_view()),
    path('create-transaction', CreateTransaction.as_view()),
]
