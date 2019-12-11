from django.urls import path
from . import views


urlpatterns = [
    path('commentviews', views.commentviews, name='commentviews'),
]
