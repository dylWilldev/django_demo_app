from django.urls import path

from . import views

urlpatterns = [
    # /home_polls/
    path("", views.home_index, name="index"),
    # /polls/#/
    path("<int:question_id>", views.detail, name="detail"),
    # /polls/#/results
    path("<int:question_id>/results", views.results, name="results"),
    # /polls/#/vote
    path("<int:question_id>/vote", views.vote, name="vote"),
]