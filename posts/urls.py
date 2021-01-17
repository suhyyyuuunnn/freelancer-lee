from django.urls import path
from .views import main, show

app_name = "posts"
urlpatterns = [
    path('main/', main, name="main"),
    path('show/', show, name="show"),
]