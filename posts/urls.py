from django.urls import path
from .views import main, show, service, detail, search

app_name = "posts"
urlpatterns = [
    path('main/', main, name="main"),
    path('show/', show, name="show"),
    path('service/', service, name="service"),
    path('detail/<int:post_id>', detail, name="detail"),
    path('search/', search, name="search"),
]