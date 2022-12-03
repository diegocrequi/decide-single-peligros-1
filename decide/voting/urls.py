from django.urls import path
from . import views


urlpatterns = [
    path('', views.VotingView.as_view(), name='voting'),
    path('<int:voting_id>/', views.VotingUpdate.as_view(), name='voting'),
    path('binaryVoting/', views.BinaryVotingView.as_view(), name='binaryVoting'),
    path('binaryVoting/<int:voting_id>/', views.BinaryVotingUpdate.as_view(), name='binaryVoting'),
]
