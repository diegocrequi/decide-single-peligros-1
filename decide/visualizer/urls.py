from django.urls import path
from .views import VisualizerView,BinaryVisualizerView


urlpatterns = [
    path('<int:voting_id>/', VisualizerView.as_view()),
    path('binaryvoting/<int:voting_id>/', BinaryVisualizerView.as_view()),
]
