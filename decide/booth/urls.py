from django.urls import path
from .views import BoothView,BinaryBoothView


urlpatterns = [
    path('<int:voting_id>/', BoothView.as_view()),
    path('binaryvoting/<int:voting_id>/', BinaryBoothView.as_view()),
]
