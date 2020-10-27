from django.urls import path
from  votingApp import views

urlpatterns = [
    path('vote',views.vote,name="vote"),
    
    
]