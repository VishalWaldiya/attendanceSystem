from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MemberListList, MemberListDetail

urlpatterns = [
    path('member/', MemberListList.as_view()),
    path('member/<int:pk>/', MemberListDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)