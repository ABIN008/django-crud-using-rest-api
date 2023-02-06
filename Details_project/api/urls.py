from django.urls import path
from api.views import DetailsList, DetailsDetail, NamesList, NamesList

urlpatterns = [
    path('data/', DetailsList.as_view()),
    path('data/<int:pk>/', DetailsDetail.as_view()),
    path('sports/',NamesList.as_view()),
    path('sports/<int:pk>/',NamesList.as_view()),
]
