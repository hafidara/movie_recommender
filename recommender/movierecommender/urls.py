from django.urls import path, include
from . import views


urlpatterns = [
    # route is a string contains a URL pattern
    path(route='', view=views.movie_recommendation_view, name='recommendations'),

]
